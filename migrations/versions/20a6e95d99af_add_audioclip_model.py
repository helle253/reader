"""add AudioClip Model

Revision ID: 20a6e95d99af
Revises: 6f5b395414a9
Create Date: 2023-12-12 13:03:23.481757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20a6e95d99af'
down_revision = '6f5b395414a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audio_clips',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_domain', sa.String(length=255), nullable=True),
    sa.Column('source_path', sa.String(length=1024), nullable=True),
    sa.Column('file_url', sa.String(length=2056), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('audio_clips')
    # ### end Alembic commands ###
