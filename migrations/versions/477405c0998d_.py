"""empty message

Revision ID: 477405c0998d
Revises: a4065ab0c573
Create Date: 2024-09-05 00:46:13.958671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '477405c0998d'
down_revision = 'a4065ab0c573'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Actuator', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sprinklerStatus', sa.Boolean(), nullable=True))
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('Sensor', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Sensor', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('Actuator', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('sprinklerStatus')

    # ### end Alembic commands ###
