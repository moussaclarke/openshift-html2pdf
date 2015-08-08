wkhmlttopdf on OpenShift
===================

I created this application to use with Pocket and IFTTT. There are some free pdf generators defined at IFTTT but some are not working and some have quantity limit to use. With free OpenShift service you can use freely.
I used wkhtmltopdf and bottle. I don't know and test what this application do under heavy load.


Running on OpenShift
----------------------------

Create an account at https://www.openshift.com/

Create a python application based on the code in this repository

    rhc app create bottle python-2.7 --from-code https://github.com/ormanli/openshift-html2pdf.git

That's it, you can now checkout your application at:

    http://bottle-$yournamespace.rhcloud.com

Download url is

    https://bottle-ormanli.rhcloud.com/pdf?url=<url-to-download>
