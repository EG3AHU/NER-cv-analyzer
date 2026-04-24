import streamlit as st
import spacy
import pdfplumber
import re
from collections import Counter

st.set_page_config(page_title='CV NLP Analysis System', layout='wide')

@st.cache_resource
def load_model():
    return spacy.load('en_core_web_sm')

nlp = load_model()

st.title('CV NLP Analysis System')
st.write('Academic project demonstrating Named Entity Recognition and spaCy linguistic features on resume documents.')

uploaded = st.file_uploader('Upload CV PDF', type=['pdf'])
manual_text = st.text_area('Or paste CV text here', height=220)


def read_pdf(file):
    text=''
    with pdfplumber.open(file) as pdf:
        for p in pdf.pages:
            text += (p.extract_text() or '') + '\n'
    return text


def email(text):
    m=re.findall(r'[\w\.-]+@[\w\.-]+',text)
    return m[0] if m else 'Not Found'


def phone(text):
    m=re.findall(r'\+?\d[\d\s\-]{8,}',text)
    return m[0] if m else 'Not Found'

text=''
if uploaded:
    text=read_pdf(uploaded)
elif manual_text.strip():
    text=manual_text.strip()

if text:
    doc=nlp(text)

    st.subheader('Candidate Information')
    lines=[x.strip() for x in text.splitlines() if x.strip()]
    st.text('Name: ' + (lines[0].title() if lines else 'Not Found'))
    st.text('Email: ' + email(text))
    st.text('Phone: ' + phone(text))

    st.subheader('Named Entity Recognition (NER)')
    ents={}
    for ent in doc.ents:
        if len(ent.text.strip())>2:
            ents.setdefault(ent.label_, set()).add(ent.text.strip())
    for k,v in ents.items():
        st.text(f'{k}: ' + ', '.join(list(v)[:10]))

    st.subheader('Linguistic Features')
    c1,c2,c3=st.columns(3)
    c1.metric('Tokens', len(doc))
    c2.metric('Sentences', len(list(doc.sents)))
    c3.metric('Unique Words', len(set([t.text.lower() for t in doc if t.is_alpha])))

    nouns=[t.lemma_.lower() for t in doc if t.pos_=='NOUN' and t.is_alpha]
    verbs=[t.lemma_.lower() for t in doc if t.pos_=='VERB' and t.is_alpha]
    adjs=[t.lemma_.lower() for t in doc if t.pos_=='ADJ' and t.is_alpha]

    st.subheader('Part of Speech Analysis')
    st.text('Top Nouns: ' + ', '.join([w for w,c in Counter(nouns).most_common(10)]))
    st.text('Top Verbs: ' + ', '.join([w for w,c in Counter(verbs).most_common(10)]))
    st.text('Top Adjectives: ' + ', '.join([w for w,c in Counter(adjs).most_common(10)]))

    st.subheader('Skills Detection')
    skills_db=['Python','SQL','Power BI','Excel','Java','C++','Git','CCNA','MCSA','DNS','ERP','Firewalls','LAN','WAN','Windows Server','TCP/IP','Networking','Technical Support','Helpdesk']
    skills=[x for x in skills_db if x.lower() in text.lower()]
    for s in skills:
        st.text('- ' + s)
    if not skills:
        st.text('No skills detected')

    st.subheader('Token Samples')
    sample=[]
    for t in doc[:20]:
        sample.append(f'{t.text} | POS:{t.pos_} | Lemma:{t.lemma_}')
    for row in sample:
        st.text(row)

    st.subheader('Resume Text')
    st.text_area('Content', text, height=250)
else:
    st.info('Upload a CV PDF or paste text to begin.')