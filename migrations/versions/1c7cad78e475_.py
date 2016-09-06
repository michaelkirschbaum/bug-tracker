"""empty message

Revision ID: 1c7cad78e475
Revises: 2095e376bae4
Create Date: 2016-09-06 00:16:29.581467

"""

# revision identifiers, used by Alembic.
revision = '1c7cad78e475'
down_revision = '2095e376bae4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracker_user', sa.Column('email', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tracker_user', 'email')
    ### end Alembic commands ###
