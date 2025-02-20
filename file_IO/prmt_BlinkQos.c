
#include "hi_cwmp_prmt.h"
#include "cwmp_utility.h"
#include "parameter_api.h"

#include "prmt_BlinkQos.h"
/*InternetGatewayDevice.X_CMCC_SmartGateway.TransferServices.BlinkQos.*/


struct CWMP_OP tBlinkQosLeafOPChilden= {getBlinkQos,setBlinkQos};
struct CWMP_PRMT tBlinkQosLeafInfo[] =
{
	{"QosEnable",  eCWMP_tBOOLEAN, CWMP_WRITE|CWMP_READ,  &tBlinkQosLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"QosParameter",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tBlinkQosLeafOPChilden, (void *)&gArea_Cmcc_Common},
};
enum eBlinkQosLeaf
{
	eBlinkQosQosEnable,
	eBlinkQosQosParameter,
};
struct CWMP_LEAF tBlinkQosLeaf[] =
{
	{&tBlinkQosLeafInfo[eBlinkQosQosEnable]},
	{&tBlinkQosLeafInfo[eBlinkQosQosParameter]},
	{ NULL }
};


int setBlinkQos(char *name, struct CWMP_LEAF *entity, int type, void *data)
{
	char *lastname = entity->info->name;
	char *buf = data;
	IgdBlinkQosTab stPara;
	IgdBlinkQosTab *pstPara = &stPara;

	if ((name == NULL) || (data == NULL) || (entity == NULL))
		return -1;
	if (entity->info->type != type)
		return ERR_9006;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdBlinkQosTab), 0, sizeof(IgdBlinkQosTab));


	if (!strcmp(lastname, tBlinkQosLeafInfo[eBlinkQosQosEnable].name))
	{
	    int *i = data;
		if (i == NULL) {
		    return ERR_9007;
		}
		if (*i < 0 || *i > 1) {
		    return ERR_9007;
		}

	    pstPara->ulBitmap = BLINKQOS_ATTR_MASK_BIT0_QOSENABLE;
	    pstPara->QosEnable = *(unsigned int *)buf;
	}else if (!strcmp(lastname, tBlinkQosLeafInfo[eBlinkQosQosParameter].name))
	{
	    if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 8) {
			return ERR_9007;
       	}

	    pstPara->ulBitmap = BLINKQOS_ATTR_MASK_BIT1_QOSPARAMETER;
	    HI_OS_STRCPY_S(pstPara->QosParameter, sizeof(pstPara->QosParameter), buf);
	}
	else
	{
		return ERR_9005;
	}

	if (pstPara->ulBitmap)
	{
		CWMP_API_SET_ENTRY_PARA_INFO_FUNC(IGD_BLINKQOS_TAB,
		                                  (UINT8 *)pstPara, 0, sizeof(stPara));
	}

	return 0;
}

int getBlinkQos(char *name, struct CWMP_LEAF *entity, int *type, void **data)
{
	char *lastname = entity->info->name;
	unsigned int msgLen = 0;
	IgdBlinkQosTab stPara;
	IgdBlinkQosTab *pstPara = &stPara;

	if ((name == NULL) || (type == NULL) || (data == NULL) || (entity == NULL))
		return -1;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdBlinkQosTab), 0, sizeof(IgdBlinkQosTab));

	msgLen = sizeof(stPara);
	pstPara->ulBitmap = QOS_ATTR_MASK_ALL;
	CWMP_API_GET_ENTRY_PARA_INFO_FUNC(IGD_BLINKQOS_TAB,
	                                  (UINT8 *)pstPara, 0, msgLen);

	*type = entity->info->type;
	*data = NULL;

	if (!strcmp(lastname, tBlinkQosLeafInfo[eBlinkQosQosEnable].name))
	{
		*data = booldup(pstPara->QosEnable);
	}
	else if (!strcmp(lastname, tBlinkQosLeafInfo[eBlinkQosQosParameter].name))
	{
		*data = strdup(pstPara->QosParameter);
	}
	else
	{
		return ERR_9005;
	}
	return 0;
}
       
