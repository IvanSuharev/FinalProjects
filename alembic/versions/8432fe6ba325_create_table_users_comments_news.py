"""create table users, comments, news

Revision ID: 8432fe6ba325
Revises: b52433f39d6c
Create Date: 2023-02-26 16:44:38.255757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8432fe6ba325"
down_revision = "b52433f39d6c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "comments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("user_id_for_comment", sa.Integer(), nullable=True),
        sa.Column("new_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["new_id"],
            ["news.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id_for_comment"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id", "description"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("comments")
    # ### end Alembic commands ###
