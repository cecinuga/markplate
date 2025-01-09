import os
import sys
from os import listdir
from markdownify import markdownify as md
from jinja2 import Environment, FileSystemLoader

if __name__ == '__main__':
    #if '--help' in sys.argv[0]:



    templateLoader = FileSystemLoader(searchpath='./templates/')
    templateEnv = Environment(loader=templateLoader)
    template_var_key = [ ]
    template_var_value = [ ]

    argv = []
    for i, arg in enumerate(sys.argv[1:]):
        if arg[0:2] != '--' and arg[0] == '-':
            template_var_key.append(arg)
            template_var_value.append(sys.argv[i+1])
        else: 
            argv.append(arg)

    #print(argv)
    #print(template_var_key)
    #print(template_var_value)

    for arg in [ '--temp', '--out', '--out-file', '--cb', '--ex-cb-dir' ]:
        if arg not in argv:
            raise SyntaxError(f'mandatory argument not submittet: {arg} ')

    for key, value in zip(argv[::2], argv[1::2]):
        print(key, value)
        match key:
            case '--temp':
                template = templateEnv.get_template(value)
            case '--out':
                outDir = value
            case '--out-file':
                outFile = value
            case '--cb':
                callback_file = value
            case '--ex-cb-dir':
                execution_callback_dir = value
            case '--exclude':
                exclude = value
            case _:
                raise SyntaxError(f'argument not valid: {key}')
    print('----------------------------------')
    loc = vars()
    callback_result = exec(open(callback_file).read(), globals(), loc)
    result = loc['result']
    #print(result)

    render = template.render(
        username='cecinuga',
        leetcodes=result
    )
    markdown = md(render)  

    output = f'{os.path.abspath(outDir)}/{outFile}'
    open(output, 'rb').close()

    with open(output, 'w') as file:
        file.write(markdown)
        file.close()
    