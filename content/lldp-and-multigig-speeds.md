Title: LLDP and multi-gig speeds
Date: 2021-10-18 06:53
Author: kmiller
Category: Work related
Tags: lldp, wi-fi
Slug: lldp-and-multigig-speeds
Status: published

So you've got that fancy new AP from VendorX with all the speeds and feeds, including multi-gigabit capability. Are you taking advantage of the increased speeds? How do you keep track of all your APs and the speeds they are linked up at? I found this interesting tidbit about LLDP when I was doing some investigation on an infrastructure insight that RUCKUS Analytics provides...

![LLDP frame from a multi-gigabit capable switch](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-3.png){.wp-image-647 width="464" height="264"}

When enabled, LLDP frames are sent by a device upon linking up. Inside of those frames is a LLDPDU that includes information fields that allow the device to identify information about itself to other devices on the LAN. Inside of the LLDPDU are a sequence of information elements (IEs) also known as TLVs that include type, length, and value fields. One of those TLVs is the *MAC/PHY Configuration/Status TLV*. Inside of this TLV, the device advertises the following things:

1. Duplex and speed (bit rate) capability  
2. Current duplex and speed settings  
3. Whether the duplex and speed settings are due to auto-negotiation during link initiation or a manual set override action

![Drill-down into the MAC/PHY Configuration/Status TLV. *PMD Auto-Negotiation Capability* is where speeds are advertised.](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-4.png){.wp-image-648 width="511" height="160"}

![Expanded list of capabilities](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-11.png){.wp-image-663 width="710" height="307"}

![R750 capable of 2.5 Gbps advertising "other"](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-14.png){.wp-image-673 width="710" height="354"}

If you read the IEEE 802.3-2018 standard, specifically subclause 79.3.1, you'll see a reference to RFC 4836 under the paragraph for PMD Auto-Negotiation Advertised Capability. This is where the bitmap of the *ifMauAutoNegCapAdvertisedBits* object or speeds that can be advertised by a device is located.

![Courtesy of [IEEE](https://ieeexplore.ieee.org/document/8457469) [802.3](https://ieeexplore.ieee.org/document/8457469)[-2018](https://ieeexplore.ieee.org/document/8457469)](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-5.png){.wp-image-650 width="735" height="108"}

Looking at RFC 4836, you'll find the *ifMauAutoNegCapAdvertisedBits* object and you can see that some capabilities are beyond the scope of it and are indicated by the value "Other". You can also see reference to the full capabilities list in the *IANAifMauAutoNegCapBits TC* or textual convention.

![Courtesy of [RFC 4638](https://datatracker.ietf.org/doc/html/rfc4836#section-3.5.4)](https://www.thepacketologist.com/wp-content/uploads/2021/10/rfc4836-capabilities-1.png){.wp-image-643 width="550" height="252"}

![Courtesy of RFC 4638](https://www.thepacketologist.com/wp-content/uploads/2021/10/rfc4836-capabilities-tc.png){.wp-image-639 width="552" height="593"}

If I interpreted all of this correctly, LLDP and its framing structure was developed before speeds greater than 1 Gbps were available. The field for advertised speed capabilities was limited to only 2 octets or 16 bits and 15 of those bits were used for other speeds including 10/100/1000. This left them with only 1 bit to use for everything else, including 2.5/5/10/25/40/50/100 Gbps. I guess the forward-thinkers weren't thinking that far out? ::shrug::

Why does this matter? In the grand scheme of things, it doesn't. I never knew this and just found it interesting. Rest assured that devices these days are capable of performing auto-negotiation without CDP or LLDP running.

![Switch and AP linked up at 2.5Gbps without LLDP](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-6.png){.wp-image-651 width="549" height="310"}

However, I mentioned I was looking into all of this as research on an insight that RUCKUS Analytics (RA) provides. Question... Is your NMS or analytics platform intelligent enough to alert you of speed mismatches between the devices on your network, including your switches and APs. When I helped manage a large, higher Ed. network, we had to run reports from our NMS to get this type of visibility and eventually I wrote a Python web app to more quickly determine the link speed of APs on a per AP Group basis. It helped that we already knew that APs should link up at 1 Gbps based on our current switching infrastructure's capabilities, so we looked for APs that were linked up at 10/100 Mbps and worked to correct the issue. Sometimes it was a bad patch cable, sometimes it was a bad switch port. This was important to us because we didn't want the LAN to be the bottleneck with regards to a Wi-Fi client's throughput. RA can handle such a task:

![Sub-optimal WAN throughput incident](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-12-1024x129.png){.wp-image-668 width="1024" height="129"}

I wish we had something at our disposal back then that would proactively alert us when our APs were running at a suboptimal speed. Suboptimal could be taken in two forms:

1.  AP is connected at a speed below what your switching infrastructure is capable of
2.  AP is not leveraging its max capable speed because your switching infrastructure doesn't support it

I imagine, you'd like to know when either of those situations are occurring for different reasons. First, you wouldn't want your LAN to be the bottleneck as I described earlier. Second, you'd also probably want to know whether you are maximizing your investment after buying those new APs with multi-gig capabilities. Especially with Wi-Fi 6E on the horizon.

Drilling down into this type of incident, you can see that we are notified when either of the two events that I mentioned above occur:

![Switching infrastructure capable of running at 100/1000 Mbps, but AP is connected at 10 Mbps](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-9.png){.wp-image-658 width="915" height="168"}

![AP is connected at 1 Gbps, but supports 2.5 Gbps](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-10.png){.wp-image-659 width="917" height="169"}

In this incident, "WAN" is from the point of view of the AP's ethernet port. Better than having to run a report or write a script or web app, right? Is this something you'd want to see? Is your NMS or analytics platform providing this to you today? If not, will you be asking for this functionality after reading this?

Let me know on [Twitter](https://twitter.com/packetologist)!

*After doing more research, I was surprised to find that RA is not using LLDP to identify these speed mismatches. This makes sense because you would want this functionality to continue to work in secure environments where LLDP might be disabled like federal government.*
