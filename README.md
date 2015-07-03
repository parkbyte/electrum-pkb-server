![Electrum-PKB-Server](https://raw.githubusercontent.com/justinvforvendetta/electrum-pkb-server/master/parkbyte.png)

electrum-pkb-server for the electrum parkbyte client
---------

  * Author: Thomas Voegtlin (Bitcoin Electrum Creator) & Sunerok (ParkByte Fork)
  * Language: Python

## ParkByte Electrum Homepage: http://electrum-pkb.net

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires parkbyted v1.1.1 or above, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of ParkByte addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-pkb-server' script



License
-------

Electrum-server is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.
