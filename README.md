Django-toollib is a common module building on top of django, include sending email, rendering template, pagination etc. 

### Sending Email

* Sending normal email  <br/>
<br/>
Programing interface: send_mail(subject, body, to, cc, use_thread=True) <br/>
Parameters: subject - the email subject <br/>
            body  - the email body <br/>
            to - the recipients (a list) <br/>
            cc - (a list) <br/>
            use_thread - whether to start a thread to send email <br/>
<br/>
A simple example demonstrating the use of the programmatic interface:
<pre>
send_mail("subject_not_use_thread", "body_not_use_thread", ["xxx@funshion.com"], [], False)
</pre>
* Sending html template email <br/>
<br/>
Programing interface: send_html_template_email(subject, template_name, data, to, cc, use_thread=True) <br/>
Parameters: template_name - the email template <br/>
            data  - the data render the template(a dictionary) <br/>
            the parameters of subject, to, cc, use_thread is the same as sending noraml email. <br/>
<br/>            
A simple example demonstrating the use of the programmatic interface:
<pre>
 send_html_template_email("template_subject_not_use_thread", 'email.html', {'username':'test'}, ["xxx@funshion.com"], [], False)
</pre>
### Rendering template and json

* render json <br/>

* render template  <br/>

### Pagination 