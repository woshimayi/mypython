#ifndef _IGD_CM_BUCPE_PUB_H_
#define _IGD_CM_BUCPE_PUB_H_

#include <igdGlobalTypeDef.h>
#include <igdCmFeatureDef.h>

#define IGD_BUCPE_TAB  (IGD_DEVICE_TAB_START + )
#define BUCPE_MAX 16


typedef struct
{
	uword32 ulStateAndIndex;
	uword32 ulIndex;

	uword8 Enable;
#define BUCPE_ATTR_MASK_BIT0_ENABLE (1<<0)
#define QOS_LIST_ATTR_MASK_ALL (0xfff)
	uword32 ulBitmap;
} __PACK__ IgdBucpeTab;


word32 igdCmBucpeGet(uword8 *pucInfo, uword32 len);
word32 igdCmBucpeSet(uword8 *pucInfo, uword32 len);
word32 igdCmBucpeInit(void);



IGDCM_OPER_REG(IGD_BUCPE_TAB, 0,  0, igdCmBucpeSet, igdCmBucpeGet, 0,  0,  0,  0, 0, 0);
#endif

IgdBucpeTab *em_Bucpe_entry = 0;
XML_DIR_ARRAY( root, em_Bucpe_entry, "EM_BUCPE_TAB", 16, IGD_BUCPE_TAB);
XML_ENTRY_PRIMITIVE2(em_Bucpe_entry, ulStateAndIndex);
XML_ENTRY_PRIMITIVE2(em_Bucpe_entry, ulIndex);
XML_ENTRY_PRIMITIVE2(em_Bucpe_entry, Enable);
XML_ENTRY_PRIMITIVE2(em_Bucpe_entry, ulBitmap);
