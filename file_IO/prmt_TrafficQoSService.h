#ifndef _PRMT_HGTRANSFERQOSSERVICEOBJECT_HG_H_
#define _PRMT_HGTRANSFERQOSSERVICEOBJECT_HG_H_


extern struct CWMP_LEAF tHgTransferQosServiceObjectLeaf[];
extern struct CWMP_NODE tHgTransferQosServiceObjectObject[];
int setHgTransferQosServiceObject(char *name, struct CWMP_LEAF *entity, int type, void *data);
int getHgTransferQosServiceObject(char *name, struct CWMP_LEAF *entity, int *type, void **data);
#endif
