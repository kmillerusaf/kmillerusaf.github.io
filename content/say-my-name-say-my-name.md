Title: "Say my name, say my name” ain’t just for Destiny’s Child
Date: 2021-10-04 08:00
Author: kmiller
Category: Wi-Fi
Tags: ruckus, wi-fi
Slug: say-my-name-say-my-name
Status: published

No, I’m not quitting my career as an IT professional to start a [R&B group](https://www.youtube.com/watch?v=sQgd6MccwZc), but hopefully the title of my blog post captured your attention enough to get you here. Now let me explain.

Earlier this year, RUCKUS released SmartZone (SZ) 6.0. There were many new features and improvements like a completely redesigned web UI for example, but another minor feature made the cut as well: AP Hostname Advertisement

![](https://www.thepacketologist.com/wp-content/uploads/2021/10/SZ-ReleaseNotes-1024x168.png){.wp-image-376}

As you can see above, the feature is disabled by default for security reasons… You wouldn’t necessarily want someone who’s performing Wi-Fi reconnaissance in your environment to discover your naming convention or know exactly where your APs are located, but this feature can come in handy for tasks like [site surveying](https://www.ekahau.com/blog/ap-name-broadcasting-2/) and troubleshooting.

Some of you may be thinking, “Keith, this isn’t anything new… My \$wifi_vendor has been doing this for years! So why should I care?”. And I’d say you’re right. It’s not new and it’s not game changing. However, from what I understand this has been a very contentious topic within RUCKUS for years so to finally have it available is great for anyone surveying or troubleshooting a RUCKUS WLAN. Also, this blog post adds value by showing you how to enable this new feature within SZ, where to look for it in the beacon or probe response frames, and what was needed to get Wireshark to decode it properly.

## Enabling the feature

To enable this feature, you’ll first need to make sure you’re working with a 6.0 zone. Yes, with RUCKUS you can have multiple zones with different firmware versions which provides a lot of flexibility when it comes to upgrading and managing your WLAN. See Jim Palmer’s [excellent blog post](https://jimswirelessworld.wordpress.com/2021/02/18/multi-generational-ap-control-with-ruckus/) on the topic if you want to learn more. You can verify the AP firmware of a zone by clicking on the zone in the left window pane and either editing it or looking down below in the “Configuration” section as shown below.

![](https://www.thepacketologist.com/wp-content/uploads/2021/10/SZ-VerifyZone-1-1024x664.jpg){.wp-image-382}

Within the 6.0 zone, create or edit a WLAN, scroll down to the “Advanced Options” section and expand it. You’ll see the “AP Host Name Advertisement in Beacon” feature. Click on the slider button next to it to enable it and click OK.

![](https://www.thepacketologist.com/wp-content/uploads/2021/10/SZ-Enable-feature-1-1024x905.png){.wp-image-383}

After clicking OK, you’ll need to wait a minute or two to allow the configuration to be pushed down to the APs in that zone and that are also advertising that specific WLAN.  Once your AP shows a configuration status of “Up-to-date”, you should be good to go.

![](https://www.thepacketologist.com/wp-content/uploads/2021/10/SZ-APs-1024x193.png){.wp-image-384}

Now how do we verify it’s working as advertised? (pun intended)

## Finding the information element in Wireshark

As the release notes mentioned, you’ll need to find the AP’s hostname in a vendor specific IE within a beacon or probe response frame. If you expand the “Tagged parameters” section under “IEEE 802.11 Wireless Management”, you’ll find the vendor specific IEs at or near the bottom of the list.

![](https://www.thepacketologist.com/wp-content/uploads/2021/10/Wireshark-1.png){.wp-image-388}

If you expand all 3 IEs to see what’s inside of them, it’ll look like the screenshot below. But where’s the name?

![](https://www.thepacketologist.com/wp-content/uploads/2021/10/Wireshark-vendorspecific-1.png){.wp-image-387}

It’s the IE that I’ve highlighted with the vendor specific OUI type of 3. How do I know this? Well, initially I guessed that it was this field and converted the vendor specific data from hex to ASCII. It turned out to be a great guess because it matched the name of my AP.

![](https://www.thepacketologist.com/wp-content/uploads/2021/10/hex-to-ascii.png){.wp-image-389}

Since this is a new and relatively minor feature, the latest releases of Wireshark from August 25, 2021 (3.4.8 and 3.2.16) do not know how to decode this information. As my good friend [Josh Schmelzle](https://twitter.com/joshschmelzle) pointed out, a dissector needed to be created for this new IE and while I’m somewhat dangerous with Python, I do not know C which is what the Wireshark dissectors are written in. Fortunately, [Adrian Granados](https://twitter.com/adriangranados) who’s written dissectors for other vendors in the past stepped in and wrote one for RUCKUS, and then submitted it to Wireshark’s GitLab repository. After about an hour or so, Adrian showed me that he had it working in [WFE Pro](https://www.intuitibits.com/products/wifi-explorer-pro/) and mentioned that it should be working in the latest [automated build](https://www.wireshark.org/download/automated/) of Wireshark’s development version. I pulled it down, fired it up, and opened the packet capture to verify. Immediately, I was able to see the difference!

![](https://www.thepacketologist.com/wp-content/uploads/2021/10/Wireshark-dev1-1.png){.wp-image-391}

![](https://www.thepacketologist.com/wp-content/uploads/2021/10/Wireshark-dev2.png){.wp-image-392}

In conclusion, SmartZone 6.0 introduced the ability to advertise an AP’s name in beacon and response frames which can be handy for site surveying and troubleshooting. This feature is disabled by default for security reasons. I’ve shown you how to enable it and where to find the name in Wireshark. In future releases of both Wireshark and WFE Pro 3, you should be able to see the decoded value of the AP’s name. Additionally, Josh is also adding the ability to see this information in his [lswifi](https://github.com/joshschmelzle/lswifi) tool for anyone who uses Windows and I highly suggest you check it out. Big thanks to both Adrian and Josh!
