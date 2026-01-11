#ifndef _PRMT_BUCPE_HG_H_
#define _PRMT_BUCPE_HG_H_


extern struct CWMP_LEAF tBucpeLeaf[];
extern struct CWMP_NODE tBucpeObject[];
int setBucpe(char *name, struct CWMP_LEAF *entity, int type, void *data);
int getBucpe(char *name, struct CWMP_LEAF *entity, int *type, void **data);
#endif
