"""empty message

Revision ID: 95d5472f33c1
Revises: 423dd1d764ae
Create Date: 2022-09-25 15:51:06.077751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95d5472f33c1'
down_revision = '423dd1d764ae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('chat_id', sa.Integer(), nullable=True))
    op.execute(f'UPDATE "user" SET chat_id = 666')
    op.alter_column('user', 'chat_id', nullable=False)
    op.drop_column('user', 'telegram_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('telegram_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('user', 'chat_id')
    # ### end Alembic commands ###
