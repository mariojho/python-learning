#!/bin/bash

if [[$# != 2]]; then
echo "usage: ./mail.sh mail_source mail_destination
exit  
fi
{
    echo "Hola smtp.univ-valenciennes.fr";
    echo "MAIL FROM:$1";
    echo "RCPT TO: $2";
    echo "data";
    echo "Message-ID: <4CDE66FB.5080406@univ-valenciennes.fr>";
    echo "Date: Thu, 27 Oct 2011 11:22:51 +0100";
    echo "From: $1";
    echo "User-Agent: Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.12) Gecko/20101027 Thunderbird/3.1.6";
    echo "MIME-Version: 1.0";
    echo "To: $2";
    echo "Subject: test eni";
    echo "Content-Type: text/plain; charset=ISO-8859-1";
    echo "Content-Transfer-Econding: 7bit";
    echo "Hola Eni";
    echo "Test de Mail";
    echo "Segunda línea";
    echo "Saludos";
    echo " ";
    echo " ";
    echo ".";
    echo " ";
    echo "QUIT";
}| nc -vv smtp.univ-valenciennes.fr 25