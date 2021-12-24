Title: ICMP Redirects and the importance of Network Analysis
Date: 2013-07-21 19:09
Author: kmiller
Category: TCP/IP, Troubleshooting
Slug: icmp-redirects-and-network-analysis
Status: published

I recently made some changes to the setup of my home network. Instead of a Linksys E3200 wireless router providing both wired and wireless access to the LAN and Internet, I added a Cisco ASA 5505 and a [Netgear GS108T](http://www.netgear.com/business/products/switches/smart-switches/smart-switches/GS108T.aspx) switch to the mix. The network now looks like this:`<!--more-->`{=html}

[![home-net](http://www.thepacketologist.com/wp-content/uploads/2013/07/home-net21-237x300.jpg){.aligncenter .size-medium .wp-image-204 width="237" height="300"}](http://www.thepacketologist.com/wp-content/uploads/2013/07/home-net21.jpg)

At first, everything appeared to be working fine; everyone in the house could get to the Internet with their devices and there were no major complaints. No SLAs broken. Great right? Well, not so fast... When I started using my laptop on the wireless network, I noticed a bit more latency getting to websites than before the changes so I decided to fire up [Wireshark](http://www.wireshark.org) to take a closer look.

Just as I suspected, I unintentionally added an additional hop to the wireless network. My wireless router was still advertising to its clients that it was the default gateway to other networks when the ASA really was. Because of this, the wireless router sent ICMP redirects to the clients informing them that there was a better option for its gateway, the ASA. This can be seen in the image below:

[![wireshark-icmp-redirect](http://www.thepacketologist.com/wp-content/uploads/2013/07/wireshark-icmp-redirect-300x179.jpg){.aligncenter .size-medium .wp-image-193 width="300" height="179"}](http://www.thepacketologist.com/wp-content/uploads/2013/07/wireshark-icmp-redirect.jpg)

Here's a sample traceroute from my laptop that displays the additional hop:

`traceroute to 208.67.222.222 (208.67.222.222), 64 hops max 1 192.168.2.254 (192.168.2.254) 3.160ms 3.835ms 2.973ms 2 X.X.X.X (X.X.X.X) 44.450ms 29.405ms 30.091ms 3 24.31.198.121 (24.31.198.121) 36.104ms 26.355ms 25.857ms 4 24.93.64.42 (24.93.64.42) 28.082ms 36.272ms 30.764ms 5 107.14.19.46 (107.14.19.46) 36.507ms 45.261ms 91.498ms 6 66.109.6.171 (66.109.6.171) 81.673ms 53.704ms 44.688ms 7 66.109.9.70 (66.109.9.70) 37.913ms 68.330ms 48.143ms 8 4.69.150.126 (4.69.150.126) 238.618ms 57.953ms 113.808ms 9 4.69.148.253 (4.69.148.253) 54.227ms 40.693ms 57.324ms 10 4.69.132.86 (4.69.132.86) 85.640ms 110.036ms 43.359ms 11 4.69.134.138 (4.69.134.138) 46.051ms 78.840ms 41.641ms 12 4.69.149.143 (4.69.149.143) 57.344ms 46.369ms 56.308ms 13 4.53.112.158 (4.53.112.158) 142.396ms 46.091ms 104.501ms 14 208.67.222.222 (208.67.222.222) 46.732ms 50.361ms 61.831ms`

So what exactly is an ICMP redirect? A simple explanation is that it is a method for a router to inform a host that a better routing option exists on the same network. For example, let's say you have Host1, RouterA, and RouterB on the same network segment. Host1's default gateway is set to RouterA and RouterA's gateway is set to RouterB. Since both routers are on the same segment as Host1, wouldn't it be more efficient to bypass RouterA and direct its packets towards RouterB? If you are nodding yes, you would be correct and ICMP redirects are the way routers convey this message to hosts.

I fixed this issue by making one small change in the firmware (DD-WRT) of my wireless router. Under the "Services" tab, I added the line ***dhcp-option=3,192.168.2.1*** in the "Additional DNSMasq Options" field to force the router to specify the ASA as the default gateway and not itself to its clients. Now a traceroute from my laptop is one hop shorter and web pages are loading more quickly. See below:

`traceroute to 208.67.222.222 (208.67.222.222), 64 hops max  1   X.X.X.X (X.X.X.X) 87.419ms 31.485ms 30.670ms   2   24.31.198.121 (24.31.198.121) 23.339ms 31.458ms 55.681ms  3   24.93.64.42 (24.93.64.42) 30.879ms 25.338ms 26.811ms  4   107.14.19.46 (107.14.19.46) 36.414ms 31.504ms 32.405ms  5   66.109.6.171 (66.109.6.171) 32.429ms 32.494ms 33.533ms  6   66.109.9.70 (66.109.9.70) 31.702ms 29.988ms 35.393ms  7   4.69.150.126 (4.69.150.126) 41.189ms 55.245ms 44.268ms  8   4.69.148.253 (4.69.148.253) 41.788ms 42.587ms 40.527ms  9   4.69.132.86 (4.69.132.86) 41.470ms 45.495ms 40.895ms  10   4.69.134.138 (4.69.134.138) 41.021ms 41.416ms 41.649ms  11   4.69.149.143 (4.69.149.143) 39.782ms 70.644ms 42.623ms  12   *  4.53.112.158 (4.53.112.158) 40.409ms 41.548ms  13   208.67.222.222 (208.67.222.222) 41.769ms 43.895ms 47.380ms`

A year or so ago, I probably wouldn't have noticed this new, small delay in my web requests let alone known why it was happening, but I credit a few things for my growth. First I credit the [TCP/IP Guide](http://www.tcpipguide.com/) where I learned what an ICMP redirect was. Second, I credit Gerald Combs and everyone who contributes to making Wireshark such an easy to use network analysis tool. Laura Chappell is someone who comes to mind as a key contributor to the Wireshark project-- If you haven't checked out her [Wireshark books](http://www.wiresharkbook.com) or free [webinars](https://www.lcuportal2.com/index.php?option=com_content&view=category&layout=blog&id=49&Itemid=75), I encourage you to do so as soon as you possibly can. The importance of network analysis cannot be overstated. Whether at home or at your place of employment, seeing the packets while you troubleshoot an issue is invaluable.

Have you ever dealt with an ICMP redirect issue? I'd love to hear about it!
