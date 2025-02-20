#include "hi_cwmp_prmt.h"
#include "cwmp_utility.h"
#include "parameter_api.h"
/*InternetGatewayDevice.X_CMCC_SmartGateway.TransferServices.BlinkQosType.{i}.*/


struct CWMP_OP tBlinkQosTypeLeafOP = { NULL ,ObjBlinkQosType};


struct CWMP_OP tBlinkQosTypeLeafOPChilden= {getBlinkQosType,setBlinkQosType};
struct CWMP_PRMT tBlinkQosTypeLeafInfo[] =
{
	{"QosPriority",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"DscpEnable",  eCWMP_tBOOLEAN, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"DscpPriority",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"Vlan8021pEnable",  eCWMP_tBOOLEAN, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"Vlan8021p",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"SourceIp",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"SourcePort",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"DestinationIp",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"DestinationPort",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"Protocol",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"SourceMac",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"DestinationMac",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tBlinkQosTypeLeafOPChilden, (void *)&gArea_Cmcc_Common},
};
enum eBlinkQosTypeLeaf
{
	eBlinkQosTypeQosPriority,
	eBlinkQosTypeDscpEnable,
	eBlinkQosTypeDscpPriority,
	eBlinkQosTypeVlan8021pEnable,
	eBlinkQosTypeVlan8021p,
	eBlinkQosTypeSourceIp,
	eBlinkQosTypeSourcePort,
	eBlinkQosTypeDestinationIp,
	eBlinkQosTypeDestinationPort,
	eBlinkQosTypeProtocol,
	eBlinkQosTypeSourceMac,
	eBlinkQosTypeDestinationMac,
};
struct CWMP_LEAF tBlinkQosTypeLeaf[] =
{
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeQosPriority]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeDscpEnable]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeDscpPriority]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeVlan8021pEnable]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeVlan8021p]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeSourceIp]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeSourcePort]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeDestinationIp]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeDestinationPort]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeProtocol]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeSourceMac]},
	{&tBlinkQosTypeLeafInfo[eBlinkQosTypeDestinationMac]},
	{ NULL }
};


struct CWMP_PRMT tBlinkQosTypeLINKObjInfo[] =
{
	{"0",  eCWMP_tOBJECT,  CWMP_READ | CWMP_WRITE | CWMP_LNKLIST,  NULL, (void *)& gArea_Cmcc_Common}
};
enum eBlinkQosTypeLINKLeaf
{
	eBlinkQosTypeLINK,
};
struct CWMP_LINKNODE tBlinkQosTypeLINKObject[] =
{
	{ &tBlinkQosTypeLINKObjInfo[eBlinkQosTypeLINK],  tBlinkQosTypeLeaf,  NULL,       NULL,           0},
	{ NULL }
};
int setBlinkQosType(char *name, struct CWMP_LEAF *entity, int type, void *data)
{
	char	*lastname = entity->info->name;
	char	*buf = data;
	unsigned int msgLen = 0;
	IgdBlinkQosTypeTab stPara;
	IgdBlinkQosTypeTab *pstPara = &stPara;
	unsigned int  instnum = 0;

	if ((name == NULL) || (data == NULL) || (entity == NULL))
		return -1;
	if (entity->info->type != type)
		return ERR_9006;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdBlinkQosTypeTab), 0, sizeof(IgdBlinkQosTypeTab));
	instnum = getCMCC_InstNum(name);
	if (instnum == 0)
		return ERR_9005;
	pstPara->ulIndex = instnum;
	printf("<%s:%d>Index[%#x]\n", __FUNCTION__, __LINE__, pstPara->ulIndex);


	if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeQosPriority].name))
	{
	    
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 7 )
		{
		    return ERR_9007;
		}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT0_QOSPRIORITY;
	    pstPara->QosPriority = *(unsigned int *)buf;
	}else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDscpEnable].name))
	{
	    int *i = data;
		if (i == NULL) {
		    return ERR_9007;
		}
		if (*i < 0 || *i > 1) {
		    return ERR_9007;
		}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT1_DSCPENABLE;
	    pstPara->DscpEnable = *(unsigned int *)buf;
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDscpPriority].name))
	{
	    
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 63 )
		{
		    return ERR_9007;
		}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT2_DSCPPRIORITY;
	    pstPara->DscpPriority = *(unsigned int *)buf;
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeVlan8021pEnable].name))
	{
	    int *i = data;
		if (i == NULL) {
		    return ERR_9007;
		}
		if (*i < 0 || *i > 1) {
		    return ERR_9007;
		}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT3_VLAN8021PENABLE;
	    pstPara->Vlan8021pEnable = *(unsigned int *)buf;
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeVlan8021p].name))
	{
	    
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 7 )
		{
		    return ERR_9007;
		}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT4_VLAN8021P;
	    pstPara->Vlan8021p = *(unsigned int *)buf;
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeSourceIp].name))
	{
	    if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 32) {
			return ERR_9007;
       	}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT5_SOURCEIP;
	    HI_OS_STRCPY_S(pstPara->SourceIp, sizeof(pstPara->SourceIp), buf);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeSourcePort].name))
	{
	    
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 65535 )
		{
		    return ERR_9007;
		}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT6_SOURCEPORT;
	    pstPara->SourcePort = *(unsigned int *)buf;
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDestinationIp].name))
	{
	    if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT7_DESTINATIONIP;
	    HI_OS_STRCPY_S(pstPara->DestinationIp, sizeof(pstPara->DestinationIp), buf);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDestinationPort].name))
	{
	    
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 65535 )
		{
		    return ERR_9007;
		}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT8_DESTINATIONPORT;
	    pstPara->DestinationPort = *(unsigned int *)buf;
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeProtocol].name))
	{
	    if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 64) {
			return ERR_9007;
       	}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT9_PROTOCOL;
	    HI_OS_STRCPY_S(pstPara->Protocol, sizeof(pstPara->Protocol), buf);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeSourceMac].name))
	{
	    if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 17) {
			return ERR_9007;
       	}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT10_SOURCEMAC;
	    HI_OS_STRCPY_S(pstPara->SourceMac, sizeof(pstPara->SourceMac), buf);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDestinationMac].name))
	{
	    if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 17) {
			return ERR_9007;
       	}

	    pstPara->ulBitmap = BLINKQOSTYPE_ATTR_MASK_BIT11_DESTINATIONMAC;
	    HI_OS_STRCPY_S(pstPara->DestinationMac, sizeof(pstPara->DestinationMac), buf);
	}
	
	msgLen = sizeof(stPara);
	CWMP_API_SET_ENTRY_PARA_INFO_FUNC(IGD_BLINKQOSTYPE_TAB, (UINT8 *)pstPara, 0, msgLen);
	return 0;
}

int getBlinkQosType(char *name, struct CWMP_LEAF *entity, int *type, void **data)
{
	char	*lastname = entity->info->name;
	unsigned int msgLen = 0;
    unsigned int  instnum = 0;
    
	if ((name == NULL) || (type == NULL) || (data == NULL) || (entity == NULL))
		return -1;

	IgdBlinkQosTypeTab stPara;
	IgdBlinkQosTypeTab *pstPara = &stPara;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdBlinkQosTypeTab), 0, sizeof(IgdBlinkQosTypeTab));
	PP("name = %s", name);
	instnum = getCMCC_InstNum(name);
	PP("instnum = %d", instnum);
	if (instnum == 0)
		return ERR_9005;
	pstPara->ulIndex = instnum;

	msgLen = sizeof(stPara);
	pstPara->ulBitmap = QOS_LIST_ATTR_MASK_ALL;
	CWMP_API_GET_ENTRY_PARA_INFO_FUNC(IGD_BLINKQOSTYPE_TAB, (UINT8 *)pstPara, 0, msgLen);
	
	*type = entity->info->type;
	*data = NULL;

	if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeQosPriority].name))
	{
		*data = uintdup(pstPara->QosPriority);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDscpEnable].name))
	{
		*data = booldup(pstPara->DscpEnable);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDscpPriority].name))
	{
		*data = uintdup(pstPara->DscpPriority);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeVlan8021pEnable].name))
	{
		*data = booldup(pstPara->Vlan8021pEnable);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeVlan8021p].name))
	{
		*data = uintdup(pstPara->Vlan8021p);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeSourceIp].name))
	{
		*data = strdup(pstPara->SourceIp);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeSourcePort].name))
	{
		*data = uintdup(pstPara->SourcePort);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDestinationIp].name))
	{
		*data = strdup(pstPara->DestinationIp);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDestinationPort].name))
	{
		*data = uintdup(pstPara->DestinationPort);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeProtocol].name))
	{
		*data = strdup(pstPara->Protocol);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeSourceMac].name))
	{
		*data = strdup(pstPara->SourceMac);
	}
	else if (!strcmp(lastname, tBlinkQosTypeLeafInfo[eBlinkQosTypeDestinationMac].name))
	{
		*data = strdup(pstPara->DestinationMac);
	}
	else
	{
		return ERR_9005;
	}
	return 0;
}
       
int ObjBlinkQosType(char *name, struct CWMP_LEAF *e, int type, void *data)
{
	struct CWMP_NODE *entity = (struct CWMP_NODE *)e;
	unsigned int ulloop;
	unsigned int msgLen = 0;
	 int ret;
	IgdBlinkQosTypeTab stPara;
	IgdBlinkQosTypeTab *pstPara = &stPara;
	IgdBlinkQosTypeTab *pstParaList = NULL;
	uint32_t *index;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdBlinkQosTypeTab), 0, sizeof(IgdBlinkQosTypeTab));
	type = (type == eCWMP_tINITOBJ)?eCWMP_tUPDATEOBJ:type;

	switch( type )
	{
	case eCWMP_tINITOBJ:
		 {
			unsigned int MaxInstNum = 0;
			struct CWMP_LINKNODE **table = (struct CWMP_LINKNODE **)data;

			if( (name==NULL) || (entity==NULL) || (data==NULL) ) return -1;

		  CWMP_API_GET_ENTRY_CNT_FUNC(IGD_BLINKQOSTYPE_TAB,&MaxInstNum);
		  CWMP_LOG(LOG_DEBUG,"INIT IGD.X_CMCC_Security.UrlFilter.obj  NUM=[%d]\n",MaxInstNum);
			if(MaxInstNum == 0)
				return 0;

			pstParaList = (IgdBlinkQosTypeTab *)malloc(MaxInstNum*sizeof(IgdBlinkQosTypeTab));
			if(NULL == pstParaList) return 0;
			HI_OS_MEMSET_S((UINT8*)pstParaList, MaxInstNum*sizeof(IgdBlinkQosTypeTab), 0, MaxInstNum*sizeof(IgdBlinkQosTypeTab));
			msgLen = MaxInstNum*sizeof(IgdBlinkQosTypeTab);

			CWMP_API_GET_ALL_ENTRY_FUNC(IGD_BLINKQOSTYPE_TAB,pstParaList,msgLen,free(pstParaList));

			for( ulloop=0; ulloop<MaxInstNum; ulloop++ )
			{
				CWMP_LOG(LOG_DEBUG,"INIT IGD.X_CMCC_Security.UrlFilter.obj	INDEX=[%d]\n",pstParaList[ulloop].ulIndex);
				if( create_Object(table, tBlinkQosTypeLINKObject, sizeof(tBlinkQosTypeLINKObject), 1, pstParaList[ulloop].ulIndex) < 0 )
				{
					 free(pstParaList);
					 return -1;
				}

			}
			//add_objectNum( name, MaxInstNum );
					 free(pstParaList);
			return 0;
		 }
	case eCWMP_tADDOBJ:
		 {
			 if( (name==NULL) || (entity==NULL) || (data==NULL) ) return -1;

			msgLen = sizeof(stPara);
			CWMP_API_ADD_ENTRY_FUNC(IGD_BLINKQOSTYPE_TAB,pstPara,msgLen);
			CWMP_LOG(LOG_DEBUG,"CM ADD IGD.X_CMCC_Security.UrlFilter.obj  INDEX=[%d]\n",pstPara->ulIndex);
			*(unsigned int*)data = pstPara->ulIndex;

			 ret = add_Object( name, (struct CWMP_LINKNODE **)&entity->next, tBlinkQosTypeLINKObject, sizeof(tBlinkQosTypeLINKObject), data );
			 HI_CWMP_LOG(CM_LOG_INFO_E, 1,"ADD %s .(inst:%d,ret:%x)", name, *(int*)data, ret);

			 return ret;
		 }

	case eCWMP_tDELOBJ:
		{
			pstPara->ulIndex = *(int*)data;
			msgLen = sizeof(stPara);
			CWMP_API_DEL_ENTRY_FUNC(IGD_BLINKQOSTYPE_TAB,pstPara,msgLen);

			ret = del_Object( name, (struct CWMP_LINKNODE **)&entity->next, *(int*)data );
			 HI_CWMP_LOG(CM_LOG_INFO_E,1, "ADD %s .(inst:%d,ret:%x)", name, *(int*)data, ret);

			return ret;
		}
	case eCWMP_tUPDATEOBJ:
		{
			unsigned int num=0, i, ulIndex = 0;
			struct CWMP_LINKNODE *old_table;

			CWMP_API_GET_ENTRY_CNT_FUNC(IGD_BLINKQOSTYPE_TAB,&num);

			CWMPDBG( 1, ( stderr, "<%s:%d>[DEBUG]:table_count is %d\n", __FUNCTION__, __LINE__, num) );
			if(num == 0)
				return 0;

			index = malloc(num * sizeof(uint32_t));
			if(NULL == index) return 0;
			(void)memset_s(index, num*sizeof(uint32_t), 0, num*sizeof(uint32_t));
			msgLen = num * sizeof(uint32_t);
			igdCmConfGetallIndex (IGD_BLINKQOSTYPE_TAB, (UINT8*)index, msgLen);

			old_table = (struct CWMP_LINKNODE *)entity->next;
			entity->next = NULL;
			for( i=0; i<num;i++ )
			{
				ulIndex = index[i];
				add_Object( name, (struct CWMP_LINKNODE **)&entity->next,  tBlinkQosTypeLINKObject, sizeof(tBlinkQosTypeLINKObject), &ulIndex );
			}
			if( old_table )
			{
				destroy_ParameterTable( (struct CWMP_NODE *)old_table );
			}
			free(index);
			return 0;
		}
	}

	return -1;
}

