from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt


from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

line_bot_api = LineBotApi('Tt/6pVp5+vesr8rBsjerS/jKvK6b0Ub0thNxIjakCH03OhFXwe2h5aTRf/ZPbWFgLvqTZGvZAkavMaGee+yqxIb3B+LxEnK7bNsJ+aNv6CnAF8Ohj76R98VDmdXm8PcqhGb1UcD4O0djVSkRsHY0qQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5d0535d7643a12130edd5db54a65d226')

@csrf_exempt
def echo(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                line_bot_api.reply_message(
                    event.reply_token,
                   TextSendMessage(text=event.message.text)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()