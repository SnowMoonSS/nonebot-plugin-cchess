"""init_db

Revision ID: 2c0cbe227dd9
Revises: 
Create Date: 2023-01-30 20:31:06.726918

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2c0cbe227dd9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_cchess_gamerecord",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("game_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("update_time", sa.DateTime(), nullable=False),
        sa.Column("player_red_id", sa.String(), nullable=False),
        sa.Column("player_red_name", sa.String(), nullable=False),
        sa.Column("player_red_is_ai", sa.Boolean(), nullable=False),
        sa.Column("player_red_level", sa.Integer(), nullable=False),
        sa.Column("player_black_id", sa.String(), nullable=False),
        sa.Column("player_black_name", sa.String(), nullable=False),
        sa.Column("player_black_is_ai", sa.Boolean(), nullable=False),
        sa.Column("player_black_level", sa.Integer(), nullable=False),
        sa.Column("start_fen", sa.String(), nullable=False),
        sa.Column("moves", sa.String(), nullable=False),
        sa.Column("is_game_over", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_cchess_gamerecord")
    # ### end Alembic commands ###
