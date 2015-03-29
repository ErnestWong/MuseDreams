class AddStateToStates < ActiveRecord::Migration
  def change
    add_column :states, :state, :integer
  end
end
