#!/usr/bin/env python3

import sys
from pyotrs import Article, Client, DynamicField, Ticket

URL = "https://url-otrs"
USER = "user"
PASSWORD = "pasword"
variable = '"OTRSTICKET"'
aspas = '"'
variableValue = aspas + ticketnumber + aspas


if(len(sys.argv) == 3):
	title = sys.argv[1]
	body = sys.argv[2]

	client = Client(URL, USER, PASSWORD)
	client.session_create()

	new_ticket = Ticket.create_basic(
				Title=title,
                                Queue="Novos tickets via telefone",
                                State=u"new",
                                Priority=u"Media prioridade",
                                CustomerUser="pbx@qosit.com.br"
				)
				
	first_article = Article({"Subject": title, "Body": body})

	create_ticket = client.ticket_create(new_ticket, first_article)

	ticketnumber = create_ticket['TicketNumber']

	variable = '"OTRSTICKET"'
	aspas = '"'
	variableValue = aspas + ticketnumber + aspas

else:
    title = " "
    body  = " "
    ticketnumber = " "

if (ticketnumber == " " or (title == " " and body == " ")):
   print("set variable \"RETURN\" \"Ticket não criado, entre em contato com nosso time de suporte!\"")
else:
   print("set variable \"RETURN\" \"Seu ticket é:\"")
   print("set variable", variable, variableValue)
