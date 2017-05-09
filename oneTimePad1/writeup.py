#!/usr/bin/env python
# coding=utf-8

from os import urandom


def num2str(n):
    return str(hex(n))[2:-1].decode('hex')


def str2num(s):
    return int(s.encode('hex'), 16)


def crypto(ctxt, secret):
    return int(ctxt, 16) ^ str2num(secret)

fake_secret1 = "I_am_not_a_secret_so_you_know_me"
fake_secret2 = "feeddeadbeefcafefeeddeadbeefcafe"
ctxt2 = "630eb4dce274d29a16f86940f2f35253477665949170ed9e8c9e828794b5543c"
ctxt3 = "e913db07cbe4f433c7cdeaac549757d23651ebdccf69d7fbdfd5dc2829334d1b"
generator2 = crypto(ctxt2, fake_secret1)
generator3 = crypto(ctxt3, fake_secret2)

f = open("generator", "w")
f.write(str(generator2) + '\n')
f.write(str(generator3) + '\n')
f.close()