FROM python:3.7

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requiremts.txt

EXPOSE 8501

COPY . .

# ENTRYPOINT ["streamlit", "run"]

# CMD ["dashboard/index.py"]
CMD streamlit run ./dashboard/index.py