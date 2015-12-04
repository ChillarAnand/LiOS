import click
import subprocess


base_url = None
last_media = None


def download_media(media_name):
    """
    Download media in url if it has content type.
    """
    url = '{}/0/{}'.format(base_url, media_name)
    cmd = 'curl -I {}'.format(url)
    result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    if 'Content-Type' in result:
        print('Downloading {}'.format(media_name))
        cmd = 'wget {} -q'.format(url)
        subprocess.call(cmd, shell=True)


def sync_media(f_type):
    """
    Download media of given f_type
    :f_type: str
    """
    if f_type == 'photos':
        media = 'fr_{}.jpg'
    if f_type == 'videos':
        media = 'fs_{}.mov'

    for i in range(last_media + 1):
        media_name = media.format(i)
        download_media(media_name)


@click.command()
@click.option('--photos', '-p', is_flag=True, help='Sync photos only')
@click.option('--videos', '-v', is_flag=True, help='Sync videos only')
@click.option('--media', '-m', is_flag=True, help='Sync photos and videos')
@click.argument('address', required=True)
def main(address, media, photos, videos):
    global base_url
    base_url = address
    print('Detecting device at {}'.format(address))
    cmd = 'wget {}/0/ -O /tmp/lios.html'.format(address)
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        if '200 OK' in result:
            print('Device detected.')
        else:
            print('Unable to detect device.')

        with open("/tmp/lios.html", "r") as fh:
            data = fh.read().replace('\n', '')

            # to get number from html like this
            # <img class="thumbnail" src="/0/tn_55.jpg"
            global last_media
            last_media = int(data.split('<img class="thumbnail" src="/0/tn_')[1].split('.jpg')[0])

    except subprocess.CalledProcessError:
        print('Unable to detect address.')

    if media:
        photos = videos = True

    if photos:
        sync_media('photos')

    if videos:
        sync_media('videos')
