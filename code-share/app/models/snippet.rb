class Snippet < ActiveRecord::Base
	validates :text, presence: true
end
