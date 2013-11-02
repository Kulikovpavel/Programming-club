class CreateSnippets < ActiveRecord::Migration
  def change
    create_table :snippets do |t|
      t.string :title
      t.string :author
      t.text :text

      t.timestamps
    end
  end
end
