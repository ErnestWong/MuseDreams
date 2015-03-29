class StatesController < ApplicationController

  def index
  end

  def show
    @state = State.find(states_params)
    respond_to do |format|
      format.html
      format.json{ render json: @state.to_json }
  end
  end

  def create
    @state = State.new(states_params)
  end

protected

  def states_params
    params.require(:state).permit(:state)
  end
end
