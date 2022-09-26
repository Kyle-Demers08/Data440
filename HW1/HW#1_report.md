# HW#1
### Kyle Demers
### Data 440, Fall 2022
### 9/27/2022

# Q1

Draw the resulting directed graph (either sketch on paper or use another tool) showing how the nodes are connected to each other and include an image in your report.

## Answer

<img width="625" alt="image" src="https://user-images.githubusercontent.com/112887807/191019192-12c3cb47-8bb0-41ec-95e1-52ea96b27576.png">


## Discussion 

# Q2

a) First, load this URI https://httpbin.org/user-agent directly in your browser and take a screenshot. The resulting webpage should show the "User-Agent" HTTP request header that your web browser sends to the web server.

b) In a single curl command, issue a HEAD HTTP request for the URI, https://t.co/EYgdZgrm2W. Show the HTTP response headers, follow any redirects, and change the User-Agent HTTP request field to "DATA 440." Show the command you issued and the result of your execution on the command line. (Either take a screenshot of your terminal or copy/paste into a code segment.)

## Answer

a) I first visited this website to find my user agent.

<img width="740" alt="image" src="https://user-images.githubusercontent.com/112887807/192108180-fe9bc9c9-3433-4f07-b527-cd29dc405c16.png">

b) I followed the redirects using this command. Note the "301" which implies that the address has been permanently moved to "Location"

<img width="880" alt="image" src="https://user-images.githubusercontent.com/112887807/192108988-b4da7946-0780-4d58-aa75-dc27b39a23a2.png">

after following the redirect, I applied the head command.

<img width="947" alt="image" src="https://user-images.githubusercontent.com/112887807/192108935-516d5ced-0384-448b-9f02-17740a6a9595.png">

I went back to the first URI to test ways to change my user agent

<img width="473" alt="image" src="https://user-images.githubusercontent.com/112887807/192109163-5c087751-f47f-45ed-b9ce-d67912360284.png">

I added the change user agent command and then revisited the 2nd website under that new user agent.

<img width="952" alt="image" src="https://user-images.githubusercontent.com/112887807/192110928-52971336-b7f5-4293-ad6f-cac164930a01.png">

## Discussion

# Q3

Write a Python program to find links to PDFs in a webpage.

Your program must do the following:

- take the URI of a webpage as a command-line argument
- extract all the links from the page
- for each link, request the URI and use the Content-Type HTTP response header to determine if the link references a PDF file
- for all links that reference a PDF file, print the original URI (found in the parent HTML page), the final URI (after any redirects), and the number of bytes in the PDF file. (Hint: Content-Length HTTP response header)

## Answer
First I imported the necessary modules being beautiful soup and requests.

<img width="539" alt="image" src="https://user-images.githubusercontent.com/112887807/192298073-0e433767-d759-403d-a5b2-b56d330df690.png">

Then I looked at all the links from the first webpage and made sure I was getting the 8 predetermined pdfs. 

<img width="527" alt="image" src="https://user-images.githubusercontent.com/112887807/192301462-3ad3c297-1bb3-478c-a831-2f391794b5c3.png">

I had to determine which ones were PDFs so I played around with the code until this worked.

<img width="245" alt="image" src="https://user-images.githubusercontent.com/112887807/192298576-cdda9bf3-598e-4e99-b1e4-ad11e4ee1815.png">

From there I had to put it all together in a function. This is the function I ended up using. The function takes the uri as a parameter.

<img width="535" alt="image" src="https://user-images.githubusercontent.com/112887807/192297561-d721c7a5-3680-40b6-9355-f740e0ddb8d4.png">

Here are the results of running the function, passing the uri as as the parameter.

<img width="749" alt="image" src="https://user-images.githubusercontent.com/112887807/192171265-4289784a-6ad3-4c27-a4dd-85f3610ca0d0.png">


## Discussion

# References

*Every report must list the references that you consulted while completing the assignment. If you consulted a webpage, you must include the URL.*

* Basic Syntax | Markdown Guide, <https://www.markdownguide.org/basic-syntax/#images-1>
* Teaching-web-science-syllabus, <https://github.com/anwala/teaching-web-science/blob/main/fall-2022/syllabus.md#summary-schedule>
* Class Piazza, <https://piazza.com/class/l3k72ehiq8z40r/post/8>
