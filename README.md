# Seans-gRPC

My gRPC experiments

## setup
```bash
git clone https://github.com/Sean-Bradley/Seans-gRPC.git
$ virtualenv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

## Start Server
```bash
python -m server
```

## Start Client
```bash
python -m client
```

While the server and 1 or more clients are running, the clients will send small messages to the server, the server will periodically log to the console how many incoming messages it received and responded to. The clients will also periodically log to the console how many they sent and got a response for. 

## Start Multiple clients in sperate processes
```bash
python -m multiprocess
```

# Video Tutorial

10000 Messages in 2.18 seconds with Python and gRPC

[![10000 Messages in 2.18 seconds with Python and gRPC](https://img.youtube.com/vi/dQK0VLahrDk/0.jpg)](https://youtu.be/dQK0VLahrDk)

# Design Patterns In Python

To help support this project, please check out my book titled **Design Patterns In Python** 

<img style="float:left; min-width:150px;" src="./img/design_patterns_in_python_book.jpg">

&nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>
&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>
&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>
&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>
&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>
&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>
&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>
&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>
&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>
&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

ASIN : B08XLJ8Z2J / B08Z282SBC

--- 

Thanks

Sean
