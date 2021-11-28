
 

<h1 style="text-align: center;color: gold;"># paypal_smartbutton_for_flask #</h1>
<h2 style="text-align: center;color: gold;">a dirty way to integrate paypal smart button to you're Flask application</h2>
<p style="text-align: center;">
    for this app you need to have some credential with paypal, for exercice and test of integration I recommended you to use you're sandbox account
</p>
<p style="text-align: center;">
    So now we have our CLIENT_ID and our SUPER_SECRET_KEY, you will need to put you're client ID into templates/button/smartbutton.html, in the first script source you will see CLIENT_ID, replace it by you're own ID
</p>
<p style="text-align: center;">
    SooOOOooOOO now I've got a problem, the problem is it didn't work on local, so we need to replace 127.0.0.1 by our not 'LOCALHOST' into the approve part of our second script into into templates/button/smartbutton.html
</p>
<p style="text-align: center;">
    We can set the price with a dynamic method into templates/button/smartbutton.html into the second script in createOrder part we can customize some parameter ( you can find it on paypal/dev) here I have just customize the price with a tiny js function lol and the currency on hard
</p>
<p style="text-align: center;">
    Now if everything is ok we can go into process.py and we can create a function for the purpose of adding our data into a DataBase.
</p>