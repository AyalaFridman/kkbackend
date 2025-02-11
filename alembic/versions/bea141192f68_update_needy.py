"""update needy

Revision ID: bea141192f68
Revises: 
Create Date: 2024-12-22 16:28:59.321847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bea141192f68'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_supports_id', table_name='supports')
    op.drop_table('supports')
    op.drop_index('ix_service_providers_id', table_name='service_providers')
    op.drop_table('service_providers')
    op.drop_index('ix_projects_id', table_name='projects')
    op.drop_table('projects')
    op.drop_index('ix_children_id', table_name='children')
    op.drop_table('children')
    op.drop_index('ix_income_id', table_name='income')
    op.drop_table('income')
    op.drop_index('ix_funds_id', table_name='funds')
    op.drop_table('funds')
    op.drop_index('ix_addresses_id', table_name='addresses')
    op.drop_table('addresses')
    op.drop_index('ix_expenses_id', table_name='expenses')
    op.drop_table('expenses')
    op.drop_index('ix_special_supports_id', table_name='special_supports')
    op.drop_table('special_supports')
    op.drop_index('ix_needy_id', table_name='needy')
    op.drop_table('needy')
    op.drop_index('ix_accounts_id', table_name='accounts')
    op.drop_table('accounts')
    op.drop_index('ix_allocations_id', table_name='allocations')
    op.drop_table('allocations')
    op.drop_index('ix_transfers_id', table_name='transfers')
    op.drop_table('transfers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transfers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('beneficiary_type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('beneficiary_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='transfers_pkey')
    )
    op.create_index('ix_transfers_id', 'transfers', ['id'], unique=False)
    op.create_table('allocations',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('allocations_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('fund_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('allocation_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('allocation_method', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('amount_or_quantity', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['fund_id'], ['funds.id'], name='allocations_fund_id_fkey'),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name='allocations_project_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='allocations_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_allocations_id', 'allocations', ['id'], unique=False)
    op.create_table('accounts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('needy_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('account_owner_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('account_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('bank_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('branch_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['needy_id'], ['needy.id'], name='accounts_needy_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='accounts_pkey')
    )
    op.create_index('ix_accounts_id', 'accounts', ['id'], unique=False)
    op.create_table('needy',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('needy_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('husband_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('id_husband', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('husband_date_of_birth', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('wife_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('id_wife', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('wife_date_of_birth', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('marital_status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('num_of_children', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('num_of_minor_children', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('num_of_unmarried_children', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('level_of_need', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('address_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('apartment_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('husband_phone', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('wife_phone', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('total_debt', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], name='needy_address_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='needy_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_needy_id', 'needy', ['id'], unique=False)
    op.create_table('special_supports',
    sa.Column('service_provider_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('needy_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('notes', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['needy_id'], ['needy.id'], name='special_supports_needy_id_fkey'),
    sa.ForeignKeyConstraint(['service_provider_id'], ['service_providers.id'], name='special_supports_service_provider_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='special_supports_pkey')
    )
    op.create_index('ix_special_supports_id', 'special_supports', ['id'], unique=False)
    op.create_table('expenses',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('needy_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('expense_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['needy_id'], ['needy.id'], name='expenses_needy_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='expenses_pkey')
    )
    op.create_index('ix_expenses_id', 'expenses', ['id'], unique=False)
    op.create_table('addresses',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('addresses_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('street', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('building_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='addresses_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_addresses_id', 'addresses', ['id'], unique=False)
    op.create_table('funds',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('funds_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='funds_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_funds_id', 'funds', ['id'], unique=False)
    op.create_table('income',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('needy_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('income_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['needy_id'], ['needy.id'], name='income_needy_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='income_pkey')
    )
    op.create_index('ix_income_id', 'income', ['id'], unique=False)
    op.create_table('children',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('needy_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('child_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['needy_id'], ['needy.id'], name='children_needy_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='children_pkey')
    )
    op.create_index('ix_children_id', 'children', ['id'], unique=False)
    op.create_table('projects',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('projects_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='projects_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_projects_id', 'projects', ['id'], unique=False)
    op.create_table('service_providers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='service_providers_pkey')
    )
    op.create_index('ix_service_providers_id', 'service_providers', ['id'], unique=False)
    op.create_table('supports',
    sa.Column('allocations_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('needy_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('notes', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['allocations_id'], ['allocations.id'], name='supports_allocations_id_fkey'),
    sa.ForeignKeyConstraint(['needy_id'], ['needy.id'], name='supports_needy_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='supports_pkey')
    )
    op.create_index('ix_supports_id', 'supports', ['id'], unique=False)
    # ### end Alembic commands ###
