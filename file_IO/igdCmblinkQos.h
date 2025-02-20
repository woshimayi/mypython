#ifndef _IGD_CM_BLINKQOS_PUB_H_
#define _IGD_CM_BLINKQOS_PUB_H_

#include <igdGlobalTypeDef.h>
#include <igdCmFeatureDef.h>

#define IGD_BLINKQOS_TAB  (IGD_DEVICE_TAB_START + )
#define BLINKQOS_MAX 16


typedef struct
{
	uword32 ulStateAndIndex;
	uword32 ulIndex;

	uword8 QosEnable;
#define BLINKQOS_ATTR_MASK_BIT0_QOSENABLE (1<<0)
	word8 QosParameter[8];
#define BLINKQOS_ATTR_MASK_BIT1_QOSPARAMETER (1<<1)
#define QOS_LIST_ATTR_MASK_ALL (0xfff)
	uword32 ulBitmap;
} __PACK__ IgdBlinkQosTab;


word32 igdCmBlinkQosGet(uword8 *pucInfo, uword32 len);
word32 igdCmBlinkQosSet(uword8 *pucInfo, uword32 len);
word32 igdCmBlinkQosInit(void);



IGDCM_OPER_REG(IGD_BLINKQOS_TAB, 0,  0, igdCmBlinkQosSet, igdCmBlinkQosGet, 0,  0,  0,  0, 0, 0);
#endif

IgdBlinkQosTab *em_BlinkQos_entry = 0;
XML_DIR_ARRAY( root, em_BlinkQos_entry, "EM_BLINKQOS_TAB", 16, IGD_BLINKQOS_TAB);
XML_ENTRY_PRIMITIVE2(em_BlinkQos_entry, ulStateAndIndex);
XML_ENTRY_PRIMITIVE2(em_BlinkQos_entry, ulIndex);
XML_ENTRY_PRIMITIVE2(em_BlinkQos_entry, QosEnable);
XML_ENTRY_UCHAR2(em_BlinkQos_entry, QosParameter);
XML_ENTRY_PRIMITIVE2(em_BlinkQos_entry, ulBitmap);
