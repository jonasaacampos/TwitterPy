<p align="center">
   <a href='https://github.com/jonasaacampos'>
      <img alt="" src="https://img.shields.io/static/v1?color=blue&label=django&message=framework&style=for-the-badge&logo=django"/>
      </a>
      <img alt="" src="https://img.shields.io/static/v1?color=green&label=python&message=programing&style=for-the-badge&logo=python"/>
      </a>
      <img alt="" src="https://img.shields.io/static/v1?color=blue&label=sqlilte&message=database&style=for-the-badge&logo=sqlite"/>
      </a>
</p>

<h1>Rede social "Twitter like" feita com django</h1>

> Rede social completa pra quem quer um twitter privado .D

<img alt="django logo" src="https://github.com/jonasaacampos/Study_Python-Django/blob/main/img/django-hexbin.png?raw=true" width=150 align=right>

[![](https://img.shields.io/badge/feito%20com%20%E2%9D%A4%20por-jaac-cyan)](https://github.com/jonasaacampos)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/jonasaacampos)

![](https://img.shields.io/badge/bulma-informational?style=flat&logo=bulma&logoColor=white&color=gold)
![](https://img.shields.io/badge/python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/django-informational?style=flat&logo=django&logoColor=white&color=black)
![](https://img.shields.io/badge/twitter-informational?style=flat&logo=twitter&logoColor=white&color=pink)

----

### Iniciar Projeto

- [ ] `python .\manage.py migrate` para criar banco de dados
- [ ] `python manage.py createsuperuser`
- [ ] `python manage.py runserver`

**Toda vez** que alterarmos o arquivo models, realizar as migrações:

- `python .\manage.py makemigrations`
- `python .\manage.py migrate`

### Ferramentas úteis

Para listar todas as possibilidades dos Forms
```python
#python .\manage.py shell
from django import forms
dir(forms)

for method in dir(forms): 
	print(method)

## para ajuda    
help(forms.CharField)
```

Forms => não gravam no banco de dados
Model Forms -> Gravam no banco de dados


<!-- CONTACT -->

## Contato

**Author:** Jonas Araujo de Avila Campos

![Alt text](https://github.com/jonasaacampos/jonasaacampos/raw/master/img/banner2.png)

<p align='center'>
  <a href='https://github.com/jonasaacampos'>
    <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'/>
  </a>
  <a href='https://www.linkedin.com/in/jonasaacampos/'>
    <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white'/>
  </a>
</p>