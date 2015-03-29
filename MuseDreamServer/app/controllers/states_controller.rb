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
    @state.save

    respond_with(@state)
  end

  def update
    @state = State.find(params[:id])
    @state.update_attributes(states_params)
    @state.save

    respond_with(@state)
  end

protected

  def states_params
    params.permit(:state)
  end
end
