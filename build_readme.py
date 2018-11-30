"""small tool to put Dockerfiles in README"""
from pathlib import Path

def _get_file(*args):
    with Path(*args).open() as fp:
        text = fp.read()
    return text

def _add_codeblock(text):
    return f"```dockerfile\n{text}\n```"

def _render_template(template, directory, text):
    return template.replace(f'{{{{ {directory} }}}}',
                            _add_codeblock(text))

def main(template_file, dirs, output_file):
    template = _get_file(template_file)
    for d in  dirs:
        template = _render_template(template,
                                    str(d),
                                    _get_file(d, 'Dockerfile')
        )
    with open(output_file, 'w') as fp:
        fp.write(template)

if __name__ == '__main__':
    template_file = '_README.md'
    dirs =  [i for i in [x for x in Path('.').iterdir() if x.is_dir()]
            if not str(i).startswith('.') and not str(i).startswith('_')]
    output_file = 'README.md'
    main(template_file, dirs, output_file)
