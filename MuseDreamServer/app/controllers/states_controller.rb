class StatesController < ApplicationController

  respond_to :json

  def index
  end

  def show
    @state = State.find(params[:id])
    respond_with(@state)
  end

  def create
    @state = State.new(states_params)
  end

protected

  def states_params
    params.require(:state).permit(:state)
  end
end
