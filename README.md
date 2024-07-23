# ETLFull

ETL Web Scraping com AWS Lambda, S3, Redshift e QuickSight
Este projeto é uma solução completa de ETL (Extract, Transform, Load) que realiza web scraping automático, armazena dados em Amazon S3, carrega os dados para Amazon Redshift e visualiza os resultados usando Amazon QuickSight.

Visão Geral
O objetivo deste projeto é coletar dados de produtos e preços de um site de e-commerce, processá-los e carregá-los em um data warehouse para análise e visualização. A arquitetura é baseada em serviços da AWS para garantir escalabilidade e eficiência.

Arquitetura
Web Scraping: Utiliza um script Python executado em AWS Lambda para realizar o scraping automático dos dados.
Armazenamento de Dados: Os dados coletados são armazenados em buckets do Amazon S3.
Processamento e Carga: Utiliza o Amazon Redshift para armazenar e processar os dados extraídos.
Visualização: Amazon QuickSight é usado para criar dashboards e visualizar os dados processados.
Componentes do Projeto
1. Web Scraping com AWS Lambda
Função Lambda: Um script Python que usa Selenium para realizar o web scraping.
Trigger: Pode ser configurado para executar em intervalos regulares usando AWS CloudWatch Events.
2. Armazenamento de Dados com Amazon S3
Bucket S3: Armazena os arquivos de dados extraídos pelo Lambda.
3. Processamento e Carga com Amazon Redshift
Cluster Redshift: Armazena os dados em um data warehouse para consultas e análises.
ETL Jobs: Scripts ou jobs que carregam os dados do S3 para o Redshift.
4. Visualização com Amazon QuickSight
Dashboards: Cria visualizações interativas dos dados processados no Redshift.
Configuração
1. Configuração do Web Scraping
Criar Função Lambda:

Suba o código Python para o Lambda.
Configure as permissões necessárias para acessar o S3.
Configurar Selenium:

Certifique-se de que o ambiente Lambda tenha os pacotes necessários para rodar o Selenium.
Configurar Trigger:

Configure um evento do CloudWatch para disparar a função Lambda em intervalos definidos.
2. Configuração do Amazon S3
Criar Bucket:

Crie um bucket no S3 para armazenar os dados extraídos.
Configurar Permissões:

Configure as permissões apropriadas para a função Lambda acessar o bucket.
3. Configuração do Amazon Redshift
Criar Cluster:

Crie um cluster Redshift.
Criar Tabelas:

Defina o esquema e crie tabelas para armazenar os dados.
Configurar ETL Jobs:

Crie scripts ou use ferramentas para carregar os dados do S3 para o Redshift.
4. Configuração do Amazon QuickSight
Conectar ao Redshift:

Configure o QuickSight para se conectar ao cluster Redshift.
Criar Dashboards:

Use o QuickSight para criar visualizações e relatórios baseados nos dados do Redshift.
Scripts e Código
lambda_function.py: Script Python para o web scraping.
etl_jobs.sql: Scripts SQL para carregar os dados no Redshift.
create_dashboard.qs: Arquivo de configuração do QuickSight (opcional).
Dependências
Python 3.x
Selenium
AWS SDK (boto3)
AWS Lambda
Amazon S3
Amazon Redshift
Amazon QuickSight
