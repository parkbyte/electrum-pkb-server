from setuptools import setup

setup(
    name="electrum-pkb-server",
    version="0.9",
    scripts=['run_electrum_pkb_server','electrum-pkb-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumpkbserver':'src'
        },
    py_modules=[
        'electrumpkbserver.__init__',
        'electrumpkbserver.utils',
        'electrumpkbserver.storage',
        'electrumpkbserver.deserialize',
        'electrumpkbserver.networks',
        'electrumpkbserver.blockchain_processor',
        'electrumpkbserver.server_processor',
        'electrumpkbserver.processor',
        'electrumpkbserver.version',
        'electrumpkbserver.ircthread',
        'electrumpkbserver.stratum_tcp',
        'electrumpkbserver.stratum_http'
    ],
    description="ParkByte Electrum Server",
    author="Thomas Voegtlin & Sunerok",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/justinvforvendetta/electrum-pkb-server/",
    long_description="""Server for the Electrum Lightweight ParkByte Wallet"""
)


