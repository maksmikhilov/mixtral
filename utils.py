import io
import pandas as pd
from contextlib import redirect_stdout

def parse_code(generate_code_result):
    start_index = generate_code_result.find('```') + 9
    end_index = generate_code_result.rfind('```')
    code = generate_code_result[start_index:end_index].strip()
    return code
    
def wrap_code_in_try_except(generate_code_result):
    try_code = "try:\n    import traceback\n    import io\n    \n"
    indented_code = '\n'.join(f"    {line}" if line else '' for line in generate_code_result.split('\n'))
    except_code = "except Exception as e:\n    f = io.StringIO()\n    traceback.print_exc(file=f)\n    err = f.getvalue()"

    wrapped_code = f"{try_code}{indented_code}\n{except_code}"
    return wrapped_code

def exec_code(generate_code_result, df):
    generate_code_result = wrap_code_in_try_except(parse_code(generate_code_result))
    variables = {'df': df, 'pd': pd}
    exec(generate_code_result, {}, variables)
    
    if variables.get('err'):
        return {
            'err': variables['err'],
            'code_result': None,
            'generate_code_result': generate_code_result
        }
    else:
        f = io.StringIO()
        with redirect_stdout(f):
            print(variables['code_result'])
        return {
            'code_result': f.getvalue(),
            'err': None,
            'generate_code_result': generate_code_result
        }

def model_request(prompt, model_params):
    
    device = "cuda"
    model = model_params['model']
    tokenizer = model_params['tokenizer']
    
    prompt = tokenizer(prompt, return_tensors="pt").to(device)
    response = model.generate(
        **prompt,
        max_new_tokens=2048,
        temperature=0.1,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(response[0], skip_special_tokens=True)