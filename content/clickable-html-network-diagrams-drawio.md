Title: Clickable HTML network diagrams with draw.io
Date: 2017-10-09 11:30
Author: kmiller
Category: Network diagrams
Slug: clickable-html-network-diagrams-drawio
Status: published

John Herbert ([\@mrtugs](https://twitter.com/@mrtugs)) over at [https://movingpackets.net](http://movingpackets.net/2017/10/03/making-clickable-html-network-diagram-using-omnigraffle/) just recently published a blog article that I felt was extremely clever and helpful. He created a clickable HTML diagram for his home network so that he could both illustrate to his wife how good of a network admin he really is and make it easier to manage the devices on his network. The only problem I saw with John’s post is that you must own [Omnigraffe](https://www.omnigroup.com/omnigraffle), a diagramming tool only supported on macOS and iOS. If you visit their website, there is a free 14-day trial to give it a spin, but it is pay-to-play software. Enter [draw.io](https://www.draw.io/) from JGraph Ltd.:

`<!--more-->`{=html}

I don’t remember exactly when draw.io came into my life, but I do believe it was brought to my attention by someone on IRC or Twitter ([*my apologies for not being able to give proper credit*]{style="color: #ff0000;"}). Since that time though, I have used [draw.io](https://www.draw.io/) several times to create some nice diagrams (including my home network) without ever having to install a single piece of software! Per their website,

> “[*draw.io is an open source technology stack for building diagramming applications, and the world’s most widely used browser-based end-user diagramming applications*]{style="color: #ff6600;"}”

That’s right, I can make some pretty cool diagrams all from my favorite web-browser… for **FREE**!

###### Let's begin.

When you first open [draw.io](https://www.draw.io/) in your web-browser, it will prompt ask you to select a destination for your saved diagrams:

\[caption id="attachment_323" align="aligncenter" width="225"\]![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-save-225x300.png "link"){.wp-image-323 .size-medium width="225" height="300"} If you aren't sure where to save the file just yet, click the Decide later button at bottom.\[/caption\]

Once you've created your diagram, it's time to add management links to the different devices.

![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-diagram-1.png){.aligncenter .wp-image-335 .size-full width="442" height="537"}

You do this by right-clicking on the object that needs a link and selecting **Edit Link…** at the bottom of the menu.

![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-editlink-1-262x300.png){.aligncenter .wp-image-331 .size-medium width="262" height="300"}

This opens a new window where you can insert the URL of your choice:

![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-link-300x115.png "link"){.aligncenter .wp-image-321 .size-medium width="300" height="115"}

Once you click apply, the URL should show below the object. If the object is not selected, it will appear as if nothing was ever done.

![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-hover-1-200x172.png){.aligncenter .wp-image-332 .size-thumbnail width="200" height="172"}

![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-nohover-1-200x170.png){.aligncenter .wp-image-333 .size-thumbnail width="200" height="170"}

After you have all of your URLs in place, it’s time to export this diagram as a HTML webpage. Start by clicking the **File** menu and selecting **HTML...** from the **Export as** sub-menu.

![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-exportashtml-249x300.png){.aligncenter .wp-image-319 .size-medium width="249" height="300"}

A new window opens allowing you to customize a few things. You can leave everything as default unless you’d like to change the border color of the objects when you hover over them. Click the **Create** button and it should open another new window prompting you for a name and where to save it to. Click the **Download** button to quickly save it to your device.

![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-customize-287x300.png){.aligncenter .wp-image-340 .size-medium width="287" height="300"}

![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-downloadhtml-294x300.png){.aligncenter .wp-image-317 .size-medium width="294" height="300"}

And here's what the final result looks like when I open the HTML file in my browser:

![](https://www.thepacketologist.com/wp-content/uploads/2017/10/drawio-html.png){.aligncenter .size-full .wp-image-336 width="428" height="579"}

Notice that nothing is highlighted until you hover over an object with an URL link configured. When I click an object (the firewall for instance), it will open a new tab in my web-browser at the address that I specified. If the link is for SSH and the OS (*e.g. macOS with Terminal app*) has a program configured to open SSH links, that program will open.

I want to conclude by giving a big shout out to John for the brilliant idea which sparked me to figure out a way to do this in [draw.io](https://www.draw.io/) and for giving me permission to piggy back off his blog post! Thanks John!
