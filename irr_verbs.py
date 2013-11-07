# coding: utf-8

words = [
u'быть', 'be-was/were-been',
u'бить', 'beat-beat-beaten',
u'становиться', 'become-became-become',
u'начинать', 'begin-began-begun',
u'согнуть(ся)', 'bend-bent-bent',
u'кусать', 'bite-bit-bitten',
u'дуть', 'blow-blew-blown',
u'(с)ломаться', 'break-broke-broken',
u'приносить', 'bring-brought-brought',
u'строить', 'build-built-built',
u'жечь, гореть', 'burn-burnt/burned-burnt/burned',
u'разрываться, прорываться, взорваться', 'burst-burst-burst',
u'покупать', 'buy-bought-bought',
u'мочь', 'can-could-been able',
u'ловить', 'catch-caught-caught',
u'выбирать', 'choose-chose-chosen',
u'приходить', 'come-came-came',
u'стоить', 'cost-cost-cost',
u'резать', 'cut-cut-cut',
u'копать', 'dig-dug-dug',
u'делать', 'do-did-done',
u'рисовать', 'draw-drew-drawn',
u'мечтать', 'dream-dreamt/dreamed-dreamt/dreamed',
u'пить', 'drink-drank-drunk',
u'воидть', 'drive-drove-driven',
u'есть', 'eat-ate-eaten',
u'падать', 'fall-fell-fallen',
u'кормить', 'feed-fed-fed',
u'чувствовать', 'feel-felt-felt',
u'бороться', 'fight-fought-fought',
u'найти', 'find-found-found',
u'летать', 'fly-flew-flown',
u'забыть', 'forget-forgot-forgotten',
u'простить', 'forgive-forgave-forgiven',
u'морозить', 'freeze-froze-frozen',
u'получить', 'get-got-got',
u'давать', 'give-gave-given',
u'идти', 'go-went-gone',
u'рости', 'grow-grew-grown',
u'висеть', 'hung-hang-hung/hanged',
u'иметь', 'have-had-had',
u'слышать', 'hear-heard-heard',
u'прятать', 'hide-hid-hidden',
u'ударять', 'hit-hit-hit',
u'держать, удерживать', 'hold-held-held',
u'причинять боль', 'hurt-hurt-hurt',
u'держать, хранить', 'keep-kept-kept',
u'знать', 'know-knew-known',
u'становиться на колени', 'kneel-knelt-knelt',
u'класть, положить', 'lay-laid-laid',
u'вести', 'lead-led-led',
u'учиться', 'learn-learnt/learned-learnt-learned',
u'оставить', 'leave-left-left',
u'отдолжить', 'lend-lent-lent',
u'позволить', 'let-let-let',
u'лежать', 'lie-lay-lain',
u'осветить', 'light-lit-lit',
u'терять', 'lose-lost-lost',
u'делать, изготавливать', 'make-made-made',
u'подразумевать, иметь в виду', 'mean-meant-meant',
u'встретить', 'meet-met-met',
u'быть должным', 'must-had to-had to',
u'платить', 'pay-paid-paid',
u'класть', 'put-put-put',
u'читать', 'read-read-read',
u'ездить верхом', 'ride-rode-ridden',
u'звонить', 'ring-rang-rung',
u'подняться', 'rise-rose-risen',
u'бежать', 'run-ran-run',
]

from random import choice


words = set(map(tuple, zip(words[::2], words[1::2])))

l = len(words)

while words:
	w = choice(list(words))
	words.remove(w)
	print '{}.'.format(l-len(words)), w[0],
	raw_input()
	print w[1]
