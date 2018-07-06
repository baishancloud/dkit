<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
#   Table of Content

- [Name](#name)
- [Status](#status)
- [Synopsis](#synopsis)
- [Description](#description)
- [Exceptions](#exceptions)
  - [ectypes.DriveIDError](#clusterdriveiderror)
  - [ectypes.BlockNotFoundError](#clusterblocknotfounderror)
  - [ectypes.BlockTypeNotSupported](#clusterblocktypenotsupported)
  - [ectypes.BlockTypeNotSupportReplica](#clusterblocktypenotsupportreplica)
  - [ectypes.BlockIndexError](#clusterblockindexerror)
- [Classes](#classes)
  - [ectypes.ReplicationConfig](#clusterreplicationconfig)
  - [ectypes.ServerID](#clusterserverid)
    - [ectypes.ServerID.validate](#clusterserveridvalidate)
  - [ectypes.DriveID](#clusterdriveid)
    - [ectypes.DriveID.validate](#clusterdriveidvalidate)
    - [ectypes.DriveID.parse](#clusterdriveidparse)
    - [ectypes.DriveID.tostr](#clusterdriveidtostr)
- [Methods](#methods)
  - [ectypes.make_serverrec](#clustermake_serverrec)
  - [ectypes.get_serverrec_str](#clusterget_serverrec_str)
  - [ectypes.validate_idc](#clustervalidate_idc)
  - [ectypes.idc_distance](#clusteridc_distance)
  - [ectypes.json_dump](#clusterjson_dump)
  - [ectypes.json_load](#clusterjson_load)
- [Classes](#classes-1)
  - [ectypes.BlockID](#clusterblockid)
    - [block id](#block-id)
    - [ectypes.BlockID.parse](#clusterblockidparse)
    - [ectypes.BlockID.`__str__`](#clusterblockid__str__)
  - [ectypes.BlockID.tostr](#clusterblockidtostr)
  - [ectypes.BlockDesc](#clusterblockdesc)
  - [ectypes.BlockGroupID](#clusterblockgroupid)
    - [block group id](#block-group-id)
    - [ectypes.BlockGroupID.parse](#clusterblockgroupidparse)
    - [ectypes.BlockGroupID.`__str__`](#clusterblockgroupid__str__)
  - [ectypes.BlockGroupID.tostr](#clusterblockgroupidtostr)
  - [ectypes.BlockGroup](#clusterblockgroup)
    - [block index](#block-index)
    - [ectypes.BlockGroup.get_block](#clusterblockgroupget_block)
    - [ectypes.BlockGroup.get_free_block_indexes](#clusterblockgroupget_free_block_indexes)
    - [ectypes.BlockGroup.mark_delete_block](#clusterblockgroupmark_delete_block)
    - [ectypes.BlockGroup.delete_block](#clusterblockgroupdelete_block)
    - [ectypes.BlockGroup.add_block](#clusterblockgroupadd_block)
    - [ectypes.BlockGroup.get_block_type](#clusterblockgroupget_block_type)
    - [ectypes.BlockGroup.get_block_idc](#clusterblockgroupget_block_idc)
    - [ectypes.BlockGroup.get_replica_indexes](#clusterblockgroupget_replica_indexes)
  - [ectypes.Region](#clusterregion)
    - [ectypes.Region.add_block](#clusterregionadd_block)
    - [ectypes.Region.move_down](#clusterregionmove_down)
    - [ectypes.Region.find_merge](#clusterregionfind_merge)
    - [ectypes.Region.list_block_ids](#clusterregionlist_block_ids)
    - [ectypes.Region.replace_block_id](#clusterregionreplace_block_id)
- [Author](#author)
- [Copyright and License](#copyright-and-license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

#   Name

ectypes

#   Status

The library is considered production ready.

#   Synopsis

```python
from pykit import ectypes

server_id = ectypes.ServerID.local_server_id()
# 12 chars from primary MAC addr: "c62d8736c728"

is_valid = ectypes.ServerID.validate(server_id)
# return True or False

serverrec = ectypes.make_serverrec('.l1', 'center', {'role1': 1}, "/s2")
# out:
#{
#   'cpu': {
#       'count': 1,
#       'frequency': 2200
#   },
#   'hostname': 'host name',
#   'idc': '.l1',
#   'idc_type': 'center',
#   'inn_ips': ['192.168.0.1'],
#   'memory': 3975237632,
#   'mountpoints': {
#       '/': {'capacity': 42140499968, 'fs': 'ext3'},
#       '/s2/drive/001': {'capacity': 5358223360, 'fs': 'xfs'},
#       '/s2/drive/002': {'capacity': 5358223360, 'fs': 'xfs'}
#   },
#   'pub_ips': ['118.1.1.1'],
#   'roles': {'role1': 1},
#   'server_id': '00163e0630f7',
#   'next_mount_index': 1,
#   "allocated_drive": {
#       "/s2/dirve/001": {"status": "normal",},
#       "/s2/dirve/002": {"status": "normal",},
#   },
#}
```

#   Description

Some helper function for the server in a ectypes.

#   Exceptions

##  ectypes.DriveIDError

**syntax**:
`ectypes.DriveIDError`

Raise if the drive id is invalid while parse it.

##  ectypes.BlockNotFoundError

**syntax**:
`ectypes.BlockNotFoundError`

Raise if a block not found in a block group.

##  ectypes.BlockTypeNotSupported

**syntax**:
`ectypes.BlockTypeNotSupported`

Raise if block index do not have corresponding type.

## ectypes.BlockTypeNotSupportReplica

**syntax**:
`ectypes.BlockTypeNotSupportReplica`

Raise if block type do not support replica.

## ectypes.BlockIndexError

**syntax**:
`ectypes.BlockIndexError`

Raise if block index parse or make error.


#   Classes


##  ectypes.ReplicationConfig

**syntax**:
`ectypes.ReplicationConfig()`

`ReplicationConfig` is a subclass of `FixedKeysDict` thus also a subclass of `dict`.
It provides the same construction function prototype as `dict`.

**keys**:

-   `in_idc`:
    An instance of namedtuple `RSConfig`, which has 2 element: N.O. of data
    and N.O. of parity.

-   `cross_idc`:
    Similar to `in_idc`, it defines cross idc EC parameter.

-   `data_replica`:
    is a number of replicas of block, before encoded with Reed Solomon.
    By default it is 1.
    And it can not be smaller than 1.

**Synopsis**:

```python
print ReplicationConfig(in_idc=[6, 2], cross_idc=[3, 1]) # {"in_idc":[6, 2], "cross_idc":[3, 1], data_replica:1}
```



##  ectypes.ServerID

**syntax**:
`ectypes.ServerID(str)`

Make a server id, format: 12 chars from primary MAC addr(e.g.: "c62d8736c728").

```python
from pykit import ectypes

print ectypes.ServerID.local_server_id()

# out: 00163e0630f7
```

### ectypes.ServerID.validate

**syntax**:
`ectypes.ServerID.validate(server_id)`

It is a classmethod for checking a server id.

**arguments**:

-   `server_id`:
    A `str` which will be checked.

**return**:
`True` or `False`, means the `server_id` is valid or not.

##  ectypes.DriveID

**syntax**:
`ectypes.DriveID(server_id, mount_point_index)`

Make a drive id, format: 16 chars `<server_id>0<mount_point_index>`

**arguments**:

    `server_id`:
    A string, Format: 12 chars from primary MAC addr.

    `mount_point_index`:
    It is a 3-digit mount path, `001` for `/drives/001`.

```python
from pykit import ectypes

print str(ectypes.DriveID('aabbccddeeff', 10))
# out: aabbccddeeff0010
```

### ectypes.DriveID.validate

**syntax**:
`ectypes.DriveID.validate(drive_id)`

It is a classmethod for checking a drive id.

**arguments**:

-   `drive_id`:
    A `str` which will be checked.

**return**:
`True` or `False`, means the `drive_id` is valid or not.

### ectypes.DriveID.parse

**syntax**:
`ectypes.DriveID.parse(drive_id)`

It is a classmethod, parse drive_id into a `namedtuple`
that contains separated fields.

Raise a `DriveIDError` if the `drive_id` is invalid.

**arguments**:

-   `drive_id`:
    A string, Format: 16 chars `<server_id>0<mount_point_index>`.

**return**:
A `namedtuple` contains `server_id` and `mount_point_index`.

###  ectypes.DriveID.tostr

**syntax**:
`ectypes.DriveID.tostr()`

Convert this DriveID instance into a string:

```python
print ectypes.DriveID('aabbccddeeff', 10).tostr()
# out: aabbccddeeff0010
```

**return**:
a string


#   Methods

##  ectypes.make_serverrec

**syntax**:
`ectypes.make_serverrec(idc, idc_type, roles, allocated_drive_pre, **argkv)`

Make a `dict` (a server record).

-   Collected physical field(pub_ips, inn_ips, hostname, server_id, memory, cpu).

-   User specified field(idc, idc_type, roles(as a dict whose values are 1), other fields if needed).

-   Mounted path(mount path, capacity, fs type).

**arguments**:

-   `idc`:
    The name of a idc in the ectypes. Format: `.l1-name.l2-name...`.

-   `idc_type`:
    Type of the idc.

-   `roles`:
    A `dict` whose values are `1`, the roles in the server.

-   `allocated_drive_pre`:
    Init status(`normal`) of the mountpoint which startswith it.

-   `argkv`:
    Other fields if needed.

**return**:
A `dict`, like:

```
{
    'cpu': {
        'count': 1,
        'frequency': 2200
    },
    'hostname': 'host name',
    'idc': '.l1',
    'idc_type': 'center',
    'inn_ips': ['192.168.0.1'],
    'memory': 3975237632,
    'mountpoints': {
        '/': {'capacity': 42140499968, 'fs': 'ext3'},
        '/s2/drive/001': {'capacity': 5358223360, 'fs': 'xfs'},
        '/s2/drive/002': {'capacity': 5358223360, 'fs': 'xfs'}
    },
    'pub_ips': ['118.1.1.1'],
    'roles': {'role1': 1},
    'server_id': '00163e0630f7'
    'next_mount_index': 1,
    "allocated_drive": {
        "/s2/dirve/001": {"status": "normal",},
        "/s2/dirve/002": {"status": "normal",},
    },
}
```

##  ectypes.get_serverrec_str

**syntax**:
`ectypes.get_serverrec_str(serverrec)`

Collect some important info(`server_id`, `idc`, `idc_type`, `roles`,
`mountpoints_count`, `allocated_drive_count`) of `serverrec` into a `str`.

**arguments**:

-   `serverrec`:
    The server record return from `ectypes.make_serverrec`.

**return**:
A `str`, like:

```
"server_id: 00aabbccddee; idc: .l1; idc_type: zz; roles: {'role1': 1}; mountpoints_count: 3; allocated_drive_count: 0"
```

##  ectypes.validate_idc

**syntax**:
`ectypes.validate_idc(idc)`

Check the name of a idc is valid or not.

**arguments**:

-   `idc`:
    The name of a idc in the ectypes. Format: `.l1-name.l2-name...`.

**return**:
`True` or `False`, means the name is valid or not.

##  ectypes.idc_distance

**syntax**:
`ectypes.idc_distance(idc_a, idc_b)`

Estimate distance between two idc.

**arguments**:

-   `idc_a`:
    First idc name.

-   `idc_b`:
    Second idc name.

**return**:
The distance of them.


##  ectypes.json_dump

**syntax**:
`ectypes.json_dump(val, encoding='utf-8')`

Implementation of `pykit.utfjson.dump`.
Preferentially convert pykit.ectypes.IDBase to string.


##  ectypes.json_load

**syntax**:
`ectypes.json_load(json_string, encoding=None)`

Implementation of `pykit.utfjson.load`.


#   Classes

##  ectypes.BlockID

**syntax**:
`BlockID(namedtuple('_BlockID', 'type block_group_id block_index drive_id block_id_seq'))`

Parse or generate block id.

### block id

`block_id`: identifies a single data or parity block.

A block is a single file on disk that contains multiple user-file.

Format: 48 chars

```
(d0|d1|d2|dp|x0|xp)<block_group_id><block_index><drive_id><block_id_seq>
2                  16              4            16        10
```

Example: `d g000630000000123 0101 c62d8736c7280002 0000000001`(without
space)


-   `type`:

    -   `d0`(data) for a `data_block`.

    -   `d1`, `d2`(the 1st and 2nd copy of data) for a `data_block`.

        If `config.ec.in_idc` config is `[4, 2]`,

        Block index of the first copy of data block `i` with `type=d1` is:
        `idc_index` `in_idc[0] + in_idc[1] + i`.

        Block index of the second copy of data block `i` with `type=d2` is:
        `idc_index` `in_idc[0] + in_idc[1] + in_idc[0] + i`.

        E.g.

        and lock `0002` has 2 copies, block indexes for these two copies are:
        `0010` and `0012`

    -   `dp`(parity of data) a in-IDC `parity_block`.

    -   `x0`(xor-parity) for a cross-IDC xor based `parity_block`.

    -   `xp`(parity of xor-parity).


    `type` layout for a block group with copies:

    ```
    data          parity  1st-copy      2nd-copy
    ----          ------  --------      --------
    d0 d0 d0 d0   dp dp   d1 d1 d1 d1   d2 d2 d2 d2
    d0 d0 d0 d0   dp dp   d1 d1 d1 d1   d2 d2 d2 d2

    x0 x0 x0 x0   xp xp
    ```

-   `block_group_id`:
    to which block group this block belongs.

-   `block_index`:
    specifies the block position in a `block_group`.
    It is a 4 digit decimal `number`:

    -   The first 2 digits is the IDC index.

    -   The latter 2 digits is the position in a IDC.

    Both these 2 parts starts from 00.

    E.g.: `block_index` of the 1st block in the first IDC is: `0000`.
    `block_index` of the 2nd block in the 3rd IDC is: `0201`.

-   `drive_id`:
    specifies the disk drive where this block resides.

-   `block_id_seq`:
    is a block group wise monotonic incremental id.
    To ensure that any two blocks have different `block_id`.

### ectypes.BlockID.parse

**syntax**:
`ectypes.BlockID.parse(block_id)`

A class method. Parse `block_id` from string to `BlockID` instanse.
If `block_id` length is wrong, `BlockIDError` raises.

**arguments**:

-   `block_id`
    block_id in string

**return**:
A `ectypes.BlockID` instance

### ectypes.BlockID.`__str__`

**syntax**:
`ectypes.BlockID.__str__()`

Rewrite `__str__`, convert `self` to `block_id` string.

**return**:
A `block_id`.

```python
block_id = 'd0g0006300000001230101c62d8736c72800020000000001'

# test parse()
bid = ectypes.BlockID.parse(block_id)
print bid.type            # d
print bid.block_group_id  # g000630000000123
print bid.block_index     # 0101
print bid.drive_id        # c62d8736c7280002
print bid.block_id_seq    # 1

# test __str__()
print bid                 # d0g0006300000001230101c62d8736c72800020000000001
```

##  ectypes.BlockID.tostr

**syntax**:
`ectypes.BlockID.tostr()`

Same as `str(ectypes.BlockID(...))`


##  ectypes.BlockDesc

**syntax**:
`ectypes.BlockDesc()`

Initialize block use a dict.

Block keys include:
    `size`: int, in byte; on-disk block file size, default is 0.
    `range`: rangeset.Range(); block range, not active range in region. Default is rangeset.Range(None, None).
    `block_id`: BlockID(). Default is None.
    `is_del`: 0 or 1. Default is 0.


##  ectypes.BlockGroupID

**syntax**:
`BlockGroupID(namedtuple('_BlockGroupID', 'block_size seq'))`

Parse or generate block group id.

### block group id

`block_group_id`: identifies a block group.

A block group is responsible of managing a group of blocks and block replication.

Format: 16 char

```
g<block_size_in_gb><seq>
 5 digit           10 digit
```

-   `block_size_in_gb`: 6 digit indicates max block size in this block group.
    Right padding with 0.

    > Thus the largest block is 99999 GB.

-   `seq`:
    zookeeper generates incremental sequence number. 10 digit, e.g.: `0000000001`.

    A `seq` is unique in a ectypes.

Example: `g 00064 0000000123`(without space).

### ectypes.BlockGroupID.parse

**syntax**:
`ectypes.BlockGroupID.parse(block_group_id)`

A class method. Parse `block_group_id` from string to `BlockGroupID` instanse.
If `block_group_id` length is wrong, `BlockGroupIDError` raises.

**arguments**:

-   `block_group_id`
    block_group_id in string

**return**:
A `ectypes.BlockGroupID` instance

### ectypes.BlockGroupID.`__str__`

**syntax**:
`ectypes.BlockGroupID.__str__()`

Rewrite `__str__`, convert `self` to `block_group_id` string.

**return**:
A `block_group_id`.

```python
block_group_id = 'g000640000000123'

# test parse()
bgid = ectypes.BlockGroupID.parse(block_group_id)
print bgid.block_size  # 64
print bgid.seq         # 123

# test __str__()
print bgid             # g000640000000123
```

##  ectypes.BlockGroupID.tostr

**syntax**:
`ectypes.BlockGroupID.tostr()`

Same as `str(ectypes.BlockGroupID(...))`

## ectypes.BlockGroup

BlockGroup meta operations.

**syntax**:
`ectypes.BlockGroup(FixedKeysDict)`

A `BlockGroup` is subclass of dict thus it shares the same construction API with
`dict`.

When initializing, the following 3 items must be specified:

- `block_group_id` is a `BlockGroupID` instance or string.
- `idcs` is a list of idc name in string.
- `config` is a `ReplicationConfig` instance or plain `dict`


### block index

`block_index`: specifies the block position in a `block_group`.

It is a 4 digit decimal `number`:

-   The first 2 digits is the IDC index.

-   The latter 2 digits is the position in a IDC.

Both these 2 parts starts from 00.

E.g.: `block_index` of the 1st block in the first IDC is: `0000`.
`block_index` of the 2nd block in the 3rd IDC is: `0201`.



### ectypes.BlockGroup.get_block

**syntax**:
`ectypes.BlockGroup.get_block(block_index, raise_error=False)`

**arguments**:

-   `block_index`:
    a string or `BlockIndex`.

-   `raise_error`:
    raise `BlockNotFoundError` if `raise_error` is `True` and block not found.
    Default is `False`

**return**:
`(block_index, block)`

### ectypes.BlockGroup.get_free_block_indexes

**syntax**:
`ectypes.BlockGroup.get_free_block_indexes(block_type=None)`

**arguments**:

-   `block_type`:
    Type of the block.

**return**
A dict that key is idc and value is a list of `block_index`.

### ectypes.BlockGroup.mark_delete_block

**syntax**:
`ectypes.BlockGroup.mark_delete_block(block_index)`

Mark a block to be `deleted` by setting its `is_del` field to `1`.

-   `block_index`:
    a string or `BlockIndex`.

**return**:
Nothing.
Will raise `BlockNotFoundError` if target block not found.


### ectypes.BlockGroup.delete_block

**syntax**:
`ectypes.BlockGroup.delete_block(block_index)`

Delete a block if it is in this group.
Do nothing if the specified block index not found.

-   `block_index`:
    a string or `BlockIndex`.

**return**:
Nothing.
Will raise `BlockNotFoundError` if target block not found.


### ectypes.BlockGroup.add_block

**syntax**:
`ectypes.BlockGroup.add_block(new_block, replace=False)`

-   `new_block`:
    is a `BlockDesc` or plain `dict` to replace.

-   `replace`:
    whether allowing to add a block at index where there is already a block.

    If it is `False` and there is a block, it raises `BlockExists`.

**return**:
a `BlockDesc` instance of the replace block.
It is `None` if there is no block at the index.

### ectypes.BlockGroup.get_block_type

**syntax**:
`ectypes.BlockGroup.get_block_type(block_index)`

-   `block_index`:
    a string or `BlockIndex`.

**return**:
block type.
Will raise `BlockTypeNotSupported` if block index do not have corresponding type.


### ectypes.BlockGroup.get_block_idc

**syntax**:
`ectypes.BlockGroup.get_block_idc(block_index=None)`

-   `block_index`:
    a string or `BlockIndex`.

**return**:
The idc in string of the block.


### ectypes.BlockGroup.get_replica_indexes

**syntax**:
`ectypes.BlockGroup.get_replica_indexes(block_index, include_me=True)`

-   `block_index`:
    a string or `BlockIndex`.

-   `include_me`:
    whether including `block_index` itself in return value

**return**:
List of data replica block index.
Will raise `BlockTypeNotSupportReplica` if block type do not support replica.


## ectypes.Region

**syntax**:
`ectypes.Region(dict)`

Region related operations.

### ectypes.Region.add_block

**syntax**:
`ectypes.Region.add_block(active_range, block, level=None)`

Add a block to a region level.

**arguments**:

-   `active_range`:
    is the active boundary of the `block` in this region. A list: `[left, right]`.

-   `block`:
    is the information of the block to add to this region. A dict:
    ```
    {
        "block_range": ["<block_left>", "<block_right>"],
        "block_id": "<block_id>",
        "size": 1234,
    }
    ```

-   `level`:
    is the region level to add `block`.
    If `level` is not specified or `None`, add block to the `max(level)+1` level.

**return**:
Nothing.

If `level` is specified but not in this region levels boundry(`0<=level<=max(level)+1`),
`LevelOutOfBound` is raised.


### ectypes.Region.move_down

**syntax**:
`ectypes.Region.move_down()`

A move includes blocks from two different, adjacent levels.
If block A overlaps with no lower level blocks, move it downward.
`move_down` moves all movable blocks in this region.

**arguments**:
Nothing

**return**:

A list of `(source_level, target_level, block)`.
This list of 3-tuple records all movable blocks which should move from
`source_level` to `target_level`.


### ectypes.Region.find_merge

**syntax**:
`ectypes.Region.find_merge()`

A merge includes blocks from two different, adjacent level.
If block A overlaps lower level blocks set s = {X, Y...}. and size(A) >= size(s)/4, merge them.
`find_merge` find one block and its overlapped blocks that can merge and return.

**arguments**:
Nothing

**return**:

-   `src_level`
    level of `src_block` that can merge downward.

-   `src_block`
    the block that can merge downward.

-   `overlapped_blocks`
    blocks in lower level that have overlap with `src_block`.

If no blocks can merge, return None.


### ectypes.Region.list_block_ids

**syntax**:
`ectypes.Region.list_block_ids(start_block_id=None)`

list all block ids in this region alphabetical from `start_block_id`.

**arguments**:

-   `start_block_id`
    used as the starting of block id list.
    If it not exists in block id list, the starting is the first one bigger than it.

**return**:
a block id list.


### ectypes.Region.replace_block_id

**syntax**:
`ectypes.Region.replace_block_id(block_id, new_block_id)`

replace block id from `block_id` to `new_block_id`.

**arguments**:

-   `block_id`
    the block id to be replaced.

-   `new_block_id`
    the block id should be replaced to.

**return**:
Nothing.
If `block_id` is not found in region levels, raise `BlockNotInRegion`.

#   Author

Baohai Liu(刘保海) <baohai.liu@baishancloud.com>

#   Copyright and License

The MIT License (MIT)

Copyright (c) 2017 Baohai Liu(刘保海) <baohai.liu@baishancloud.com>