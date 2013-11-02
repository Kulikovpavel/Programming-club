class SnippetsController < ApplicationController
	http_basic_authenticate_with name: "admin", password: "secsec", only: :destroy

	def new
	end

	def create
		@snippet = Snippet.new(snippet_params)
 
		@snippet.save
		redirect_to @snippet
	end

	def show
  		@snippet = Snippet.find(params[:id])
	end

	def index
  		@snippets = Snippet.all
	end

	def destroy
  		@snippet = Snippet.find(params[:id])
  		@snippet.destroy
 
  		redirect_to snippets_path
	end

	private
  		def snippet_params
    		params.require(:snippet).permit(:title, :author, :text)
  		end
end
