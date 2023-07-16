from alembic import op
import sqlalchemy as sa

revision = '569227472afd'
down_revision = None
branch_labels = None
depends_on = None


def create_statistic_table() -> None:
    op.create_table(
        "t",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("x", sa.Integer),
        sa.Column("y", sa.Integer),
        sa.Column("d", sa.DateTime())
    )


def upgrade() -> None:
    create_statistic_table()


def downgrade() -> None:
    op.drop_table("cleanings")
