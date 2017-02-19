import operator
import pprint
import subprocess


def main():
    def line2info(ps_line):
        fields = ps_line.split(None, 2)
        return dict(pcpu=fields[0], rss=fields[1], comm=fields[2])

    ps_bytes = subprocess.check_output(
        'ps -e -o pcpu,rss,comm --no-headers --sort=-pcpu | head',
        shell=True)
    ps_text = ps_bytes.decode()
    ps_lines = ps_text.split('\n')
    ps_info = [line2info(line) for line in ps_lines if line]
    pprint.pprint(ps_info)
    print()

    print('LARGEST RESIDENT SIZE')
    ps_info = sorted(ps_info, key=operator.itemgetter('rss'),
        reverse=True)  # noqa
    pprint.pprint(ps_info[:2])


if __name__ == '__main__':
    main()
