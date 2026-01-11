#ifndef _IGD_CM_HGTRANSFERQOSSERVICEOBJECT_PUB_H_
#define _IGD_CM_HGTRANSFERQOSSERVICEOBJECT_PUB_H_

#include <igdGlobalTypeDef.h>
#include <igdCmFeatureDef.h>

#define IGD_HGTRANSFERQOSSERVICEOBJECT_TAB  (IGD_DEVICE_TAB_START + )
#define HGTRANSFERQOSSERVICEOBJECT_MAX 16


typedef struct
{
	uword32 ulStateAndIndex;
	uword32 ulIndex;

#define QOS_LIST_ATTR_MASK_ALL (0xfff)
	uword32 ulBitmap;
} __PACK__ IgdHgTransferQosServiceObjectTab;


word32 igdCmHgTransferQosServiceObjectGet(uword8 *pucInfo, uword32 len);
word32 igdCmHgTransferQosServiceObjectSet(uword8 *pucInfo, uword32 len);
word32 igdCmHgTransferQosServiceObjectInit(void);



IGDCM_OPER_REG(IGD_HGTRANSFERQOSSERVICEOBJECT_TAB, 0,  0, igdCmHgTransferQosServiceObjectSet, igdCmHgTransferQosServiceObjectGet, 0,  0,  0,  0, 0, 0);
#endif

IgdHgTransferQosServiceObjectTab *em_HgTransferQosServiceObject_entry = 0;
XML_DIR_ARRAY( root, em_HgTransferQosServiceObject_entry, "EM_HGTRANSFERQOSSERVICEOBJECT_TAB", 16, IGD_HGTRANSFERQOSSERVICEOBJECT_TAB);
XML_ENTRY_PRIMITIVE2(em_HgTransferQosServiceObject_entry, ulStateAndIndex);
XML_ENTRY_PRIMITIVE2(em_HgTransferQosServiceObject_entry, ulIndex);
XML_ENTRY_PRIMITIVE2(em_HgTransferQosServiceObject_entry, ulBitmap);
