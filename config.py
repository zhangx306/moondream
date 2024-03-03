default_prompt = """
Assuming you are a store assistant please analyze the item in the picture.
 Only return the data in a json with the keys shape, dominant_colors, style, description, material, suggested_title, theme. 
 Please restrict the product description to 100 words. 
 For theme please return any special characteristics like nature, geometric, abstract etc. 
"""

gpt4_res_json_path = "inferences/description_by_gpt4.json"

moondream_res_csv_path = "inferences/description_by_moondream.csv" 
gpt4_res_csv_path = "inferences/description_by_gpt4.csv"
both_res_csv_path = "inferences/description_by_both.csv"