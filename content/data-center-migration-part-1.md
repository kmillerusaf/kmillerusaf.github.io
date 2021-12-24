Title: Data center migration - Part 1
Date: 2013-01-23 13:41
Author: kmiller
Category: Uncategorized, Work related
Slug: data-center-migration-part-1
Status: published

*Full disclosure: This is only my 2nd experience with migrating a data center and the first time I was working with a much smaller network and infrastructure in general with a stacked pair of 3750s using static routes, some L2 2960s and a couple of ASA 5510s.*

This last experience is what I'll be writing about. But first, let me give you some background on the data center before we moved. `<!--more-->`{=html}Our core was a pair of 6509s using VSS with a pair of stacked 3750s at the top of each server rack. We used 2x10G links in an etherchannel from the 6500s to each stack of 3750s which was plenty of bandwidth for our traffic in my opinion. I don't have any graphs or performance monitoring to back that up, so I'm going off of my own mileage. We have just migrated from Cisco Works to Cisco Prime but with all the projects right now, we don't have the time to truly see the power of Prime and if it can do what we need it to do. Also, other networking equipment exists, however they were not changed during the move so I will not comment on them.

Now to the interesting part. First, the migration was two-fold; we were moving our data center from one building to another because of power and HVAC issues in the former and we were changing our platform from the 6500s/3750s to Nexus 7Ks, 5Ks, and FEXs. Moving to Nexus really wasn't a decision made for any other reason than to share equipment with another network shop that had already bought the equipment. Initially there was some push back, because we were going away from the standard which was using the Catalyst switches but eventually it was approved and we pushed forward. So a couple of us were sent to a Nexus boot camp in April of 2012 to spin up on the new platform since none of us had used it previously. I was very intrigued and interested, however, I felt like a 4 day boot was not enough time to get hands on experience and learn everything that we would need to know to completely change the infrastructure of our data center. That was my first experience with boot camps and I can say that I'm not a big fan of them but I'll save that for another post somewhere along the line. Roughly 7 months later the new building was completely constructed and ready for us to start staging and configuring equipment. None of us had touched the CLI since April or ever seen the gear physically in person. I was certainly impressed by the shear size of the 7K and 5Ks. We are talking about a device (7K) which is 200 pounds without any modules installed. It can exceed 500 pounds fully stocked. The 5Ks are as long as normal servers are and take up the length of the rack. Anyway, I'll touch more on my impressions of the gear in part 2 of this post. So I went back to the book materials given to us in April and started brushing upon what I had already forgotten. It started coming back to me and I was beginning to feel more confident about the migration. As I started configuring the devices, however, I kept running into difference after difference between the way NX-OS was configured and operated vs IOS. I won't touch on them all but here are a few things that I ran into (good or bad) with the hope that this helps someone who's looking to move to Nexus:

```{=html}
<ol>
```
-   [NTP on the 7K can only be configured from the default VDC. This is an issue for us because we do not control the default VDC so we'll have to eventually configure connectivity between the 2 VDCs in order to pull time from our hardware time appliance. From Cisco's ]{style="line-height: 1.714285714; font-size: 1rem;"}[site](http://www.cisco.com/en/US/docs/switches/datacenter/sw/4_2/nx-os/system_management/configuration/guide/sm_3ntp.html)[,]{style="line-height: 1.714285714; font-size: 1rem;"}[ "]{style="line-height: 1.714285714; font-size: 1rem;"}[You must configure NTP in the default VDC.".]{style="line-height: 1.714285714; font-size: 1rem;"}

```{=html}
</ol>
```
```{=html}
<ol>
```
-   [Network statements inside the router process for EIGRP and OSPF are not supported and you advertise the network by placing a command on the L3 interface (e.g. ip router eigrp 1). Passive-interfaces are also configured inside the interfaces.]{style="font-size: 1rem; line-height: 1.714285714;"}

```{=html}
</ol>
```
[![no_ntwrk_eigrp](http://www.thepacketologist.com/wp-content/uploads/2013/01/no_ntwrk_eigrp-300x31.jpg){.aligncenter .size-medium .wp-image-28 width="300" height="25"}](http://www.thepacketologist.com/2013/01/data-center-migration-part-1/no_ntwrk_eigrp/)

```{=html}
<ol>
```
-   [No more unicast neighbor statements with EIGRP or OSPF. I know this shouldn't be needed in most circumstances, however we manage a network with hardware encryption devices that don't pass multicast packets; our work around for this was using the neighbor statements for each expected neighbor. Since we could no longer rely on this, we had 2 options. Use GRE tunnels or put a Catalyst device that supported this command in front of the 7K. Since we found out about this so late in the process, we went with the latter and put 2911 routers in front of the 7K to avoid having to re-engineer our network on the fly.]{style="font-size: 1rem; line-height: 1.714285714;"}

```{=html}
</ol>
```
[![no_neighbor_eigrp](http://www.thepacketologist.com/wp-content/uploads/2013/01/no_neighbor_eigrp-300x25.jpg){.aligncenter .size-medium .wp-image-27 width="300" height="25"}](http://www.thepacketologist.com/2013/01/data-center-migration-part-1/no_neighbor_eigrp/)

-   [No more need for the 'do' command when trying to perform show commands from global config mode or another specific configuration mode. That's right, just like the Cisco ASA's OS for those of you familiar with it, you can run the commands from anywhere. Also, if you run a command that isn't found in that level of configuration, the OS will attempt to find a match command in levels below it and if found, apply it there.]{style="font-size: 1rem; line-height: 1.714285714;"}

[![do_from_anywhere](http://www.thepacketologist.com/wp-content/uploads/2013/01/do_from_anywhere-300x155.jpg){.aligncenter .size-medium .wp-image-26 width="300" height="155"}](http://www.thepacketologist.com/2013/01/data-center-migration-part-1/do_from_anywhere/)

-   In IOS, AAA can be configured using the TACACS+ protocol where you can use the default group "TACACS+" when you want to use all of the specified TACACS+ servers. In NX-OS, you must create the group first and specify the servers inside of the group before you are allowed to use them.

There are definitely more differences out there but I won't cover them all here. If you have run into any good ones, feel free to share. I will give my impressions of the Nexus gear and overall experience in part 2 of this post. Stay tuned and thanks for reading!
