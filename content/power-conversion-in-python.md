Title: Building a power conversion tool in Python
Date: 2021-10-25 09:22
Author: kmiller
Category: Wi-Fi
Tags: python, wi-fi
Slug: power-conversion-in-python
Status: published

I’ve been doing less and less Python development since moving to a new company back in June. At my previous employer, I worked on Python command-line scripts and a custom-built web app fairly often that assisted with daily, monotonous tasks as well as troubleshooting. I really enjoyed the process of learning more about Python and developing tools that helped not just myself, but also my team.

A couple of months ago, I was reading something and power was given in milliwatts instead of dBm. I wanted to convert the values to dBm since it's the unit I'm most comfortable with and while I’m very familiar with the rule of 10s and 3s, sometimes I want the exact conversion or I want the number quickly; 10s and 3s doesn’t always give you that. I’m aware that there are [online tools](https://www.rapidtables.com/convert/power/dBm_to_mW.html) that do this very same task, but because it had been a little while since I wrote anything meaningful in Python, I thought it would be a good exercise for me to keep my coding skills somewhat sharp. After all, I live by the “if you don’t use it, you’ll lose it” philosophy.

As a reminder, here are the rules for 10s and 3s:

-   For every 10 dB of gain, multiply the mW value by 10.
-   For every 3 dB of gain, multiply the mW value by 2.
-   For every 3 dB of loss, divide the mW value by 2.
-   For every 10 dB of loss, divide the mW value by 10.

Reference value: 1 mW = 0 dBm

If you want to convert dBm to mW exactly, the formula is:  
`P(mW) = 1mW * 10(P(dBm)/ 10)`

If you want to convert mW to dBm exactly, the formula is:  
`P(dBm) = 10 * log10(P(mW) / 1 mW)`

The general idea was to be able to input power in either mW or dBm and convert the value to the opposite unit of measure. Simple enough.

By just importing the math module and creating a couple of small functions, I'm now able to quickly convert between absolute and relative power.

![`<meta charset="utf-8">`{=html} ¶ It only took 61 lines of code to have a basic Python scrip that converts between 2 units of power](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-31-642x1024.png){.wp-image-721 width="642" height="1024"}

![Converting from dBm to mW and mW to dBm](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-28.png){.wp-image-715 width="641" height="313"}

If I performed the conversion using the rule of 10s and 3s, the values would be very close as you can see in the table below, but not exact. In addition, I find it harder to convert from mW to dBm when doing it in my head. I think most would agree that the process of using 10s and 3s would typically take longer than just using the script, a conversion table, or an online tool.

![Table courtesy of [WLAN Pros](https://www.wlanprofessionals.com)](https://www.thepacketologist.com/wp-content/uploads/2021/10/image-24.png){.wp-image-705 width="553" height="379"}

After recently participating in a 24-hour codeathon at work, I became familiar with one of Python’s GUI libraries, [PyQt5](https://www.riverbankcomputing.com/software/pyqt/). What I like about PyQt5 is that it helps you a build a cross-platform UI that looks and feels pretty much the same whether you're on Linux, macOS, Windows, iOS, or Android. I thought it might be nice to build a simple UI for this script, but I’m struggling to see the value in it. The CLI script is simple and quick enough and there’s already several online tools available that can do this. Maybe I’ll do it just to get more experience with PyQt5, but if there’s any real interest in having a UI, I might be more inclined to do it.

I actually had a thought while writing this... Are there any Python-based tools out there that combine the various tasks that Wi-Fi engineers have to perform like power conversion, FSPL, link budget, etc? I know there are websites for them, but it would be nice to have something locally on your machine that combines all of these tools in one place, especially if you find yourself somewhere with no Internet access (rare these days, I know). What do you all think? Any interest?

Reach out on [Twittter](https://twitter.com/packetologist)!

\*\*\* EDIT \*\*\* Thanks to Jake Snyder for suggesting I use argparse for command line parameters to help speed things up. I had thought about doing it previously because I know how much it can help, but elected not to. Shortly after he mentioned it to me on Twitter, I went ahead and updated the code and posted new screenshots above. This is what I like about Twitter, idea sharing.
