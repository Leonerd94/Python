import requests
import sys
import json
import argparse


parser = argparse.ArgumentParser('zoo client')
parser.add_argument('command')
parser.add_argument('--nome')
args = parser.parse_args()

if args.command == 'store':
    store_animal(args.nome)
elif args.command == 'list':
    list_all()
elif args.command == 'count':
    count(args.nome)
else:
    print 'Errore'

HOTS = 'localhost'

def store_animal(nome):
    resp = requests.post(
        'http://{}/zoo'.format(HOST),
        json.dumps({'nome':nome}))

    if resp.status_code == 200:
        print 'OK'
    else: 
        print 'Errore'

def list_all():
    resp = requests.get('http://{}/zoo'.format(HOST))
    content = json.loads(resp.content)
    for animal in content:
        print animal['nome']+'\n'
        
def count(nome):
    resp = requests.get('http://{}/zoo'.format(HOST))
    content = json.loads(resp.content)
    cnt = 0
    for animal in content:
        if(animal['nome'] == nome):
            cnt += 1
    print 'Number of {}: {}'.format(nome, cnt)