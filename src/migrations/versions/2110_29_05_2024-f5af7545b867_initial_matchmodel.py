"""initial_matchmodel

Revision ID: f5af7545b867
Revises: f8ba1428581c
Create Date: 2024-05-29 21:10:07.906953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5af7545b867'
down_revision: Union[str, None] = 'f8ba1428581c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('urls', 'url',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('vacancies', 'vacancy_vector',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vacancies', 'vacancy_vector',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('urls', 'url',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    # ### end Alembic commands ###
