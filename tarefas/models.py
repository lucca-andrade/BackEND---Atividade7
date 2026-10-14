from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):

    PRIORIDADES = [
        ('ALTA', 'Alta'),
        ('MEDIA', 'Média'),
        ('BAIXA', 'Baixa')
    ]

    SITUACOES = [
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDA', 'Concluída')
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADES
    )

    data_prevista = models.DateField()

    situacao = models.CharField(
        max_length=15,
        choices=SITUACOES
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo